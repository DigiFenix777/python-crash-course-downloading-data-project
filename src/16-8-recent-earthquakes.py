# 16.8 - Recent Earthquakes: 30 days of magnitude 4.5+ earthquake data from July 9 - Aug 9, 2025
# Includes Kamchatka 8.8 magnitude earthquake on July 29, 2025.
from pathlib import Path
import json
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, UTC

# Read data as a string and convert it to a Python object.
path = Path('../earthquake_data/eq_data_past_30_days_m4plus.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('../earthquake_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# OPTIONAL - Use Try/Except to prevent plotly from crashing for magnitude None values.
rows = []
for eq in all_eq_dicts:
    try:
        mag = eq["properties"]["mag"]
        lon, lat = eq["geometry"]["coordinates"][:2]
        title = eq["properties"]["title"]
        ts_ms = eq["properties"]["time"]  # epoch ms
        if mag is None or ts_ms is None:
            raise ValueError("Missing mag or time")
        date_str = datetime.fromtimestamp(ts_ms / 1000, tz=UTC).strftime("%Y-%m-%d %H:%M UTC")
        rows.append((mag, lon, lat, title, date_str))
    except (ValueError, TypeError, IndexError):
        continue

# Build and sort DataFrame.
df = pd.DataFrame(rows, columns=["mag","lon","lat","title","date"])
df = df.sort_values("mag", ascending=True)

# Size dots logarithmically to align with Richter scale.
mmin, mmax = df["mag"].min(), df["mag"].max()

# Choose ONE of these mappings:

# A) Balanced (more separation than linear, still readable on small screens)
# gamma = 1.6  # >1 exaggerates differences; try 1.4–1.8
# rel = ((df["mag"] - mmin) / (mmax - mmin)) ** gamma

# B) Flattened (so sizes aren’t wildly different; good for dense maps)
# gamma = 0.8  # <1 flattens differences
# rel = ((df["mag"] - mmin) / (mmax - mmin)) ** gamma

# C) Exaggerated separation to emphasize differences in magnitude.
gamma = 2.13  # exaggerated separation
rel = ((df["mag"] - mmin) / (mmax - mmin)) ** gamma
sizes = np.interp(rel, (rel.min(), rel.max()), (10, 50))  # adjust min/max px if needed

# D) Richter-ish (energy grows ~10^(1.5M) — then compress to screen)
# rel = 10 ** (1.5 * (df["mag"] - mmin))

# Normalize rel → pixel sizes in a nice on-screen range
# sizes = np.interp(rel, (rel.min(), rel.max()), (10, 44))

# make sure df["date"] exists (your UTC fix)
# customdata: [date, lat, lon]  -> indices 0,1,2
fig = go.Figure(go.Scattergeo(
    lon=df["lon"], lat=df["lat"], mode="markers",
    text=df["title"],  # Title first line
    customdata=np.c_[df["date"], df["lat"], df["lon"]],
    marker=dict(
        size=sizes,
        color=df["mag"],
        colorscale="Inferno",
        cmin=mmin, cmax=mmax,
        opacity=0.9,
        line=dict(width=0),
        colorbar=dict(title="Magnitude"),
    ),
))

# One hovertemplate only: Title > Date > Lat/Long
fig.update_traces(
    hovertemplate="%{text}<br>"
                  "%{customdata[0]}<br>"
                  "Lat: %{customdata[1]:.2f}, Lon: %{customdata[2]:.2f}"
                  "<extra></extra>"
)

fig.show()



# 16.9 - World Fires:
from pathlib import Path
import csv
import numpy as np
import plotly.graph_objects as go

# Read data
path = Path('../wildfire_data/world_fires_7_day.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract data
lats, lons, brights, frps = [], [], [], []
for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    bright = float(row[2])
    frp = float(row[11])
    lats.append(lat)
    lons.append(lon)
    brights.append(bright)
    frps.append(frp)

# Build the plot
# arrays: lats, lons, brights, frps
lat = np.asarray(lats, float); lon = np.asarray(lons, float)
br  = np.asarray(brights, float); fr = np.asarray(frps, float)
m = ~(np.isnan(lat)|np.isnan(lon)|np.isnan(br)|np.isnan(fr))
lat, lon, br, fr = lat[m], lon[m], br[m], fr[m]

# --- color driver: brightness ---
br_c = np.clip(br, 300, 450)                        # fixed range for comparability
b_norm = (br_c - 300) / (150 + 1e-9)

# --- FRP preprocessing (for size & opacity) ---
fr_cap  = np.percentile(fr, 99) if fr.size else 0.0
fr_c    = np.clip(fr, 0, fr_cap)
fr_log  = np.log1p(fr_c)
fr_min, fr_max = fr_log.min(), fr_log.max()
f_norm  = (fr_log - fr_min) / (fr_max - fr_min + 1e-9)

# --- size from your existing intensity (FRP-biased geometric mean) ---
alpha = 0.75
I = (f_norm**alpha) * (b_norm**(1 - alpha))         # keep same "intensity" calc
gamma_size = 0.85
SIZE_MIN, SIZE_MAX = 2, 8
sizes_px = SIZE_MIN + (I**gamma_size) * (SIZE_MAX - SIZE_MIN)

# --- opacity from FRP ONLY (quantile bands, low FRP = faint) ---
qF = np.linspace(0,1,6) if np.allclose(f_norm.min(), f_norm.max()) \
     else np.quantile(f_norm, [0,.2,.4,.6,.8,1.0])
f_band = np.searchsorted(qF, f_norm, side="right") - 1
f_band = np.clip(f_band, 0, 4)
opacities = np.array([0.10, 0.22, 0.40, 0.65, 0.95])  # softer lows, solid highs

# --- draw order by BRIGHTNESS so yellows land on top ---
qB = np.linspace(300,450,6) if np.allclose(br_c.min(), br_c.max()) \
     else np.quantile(br_c, [0,.2,.4,.6,.8,1.0])
b_band = np.searchsorted(qB, br_c, side="right") - 1
b_band = np.clip(b_band, 0, 4)

fig = go.Figure()

# Cool → hot; within each brightness band, low-FRP → high-FRP; small → large
for bb in range(5):
    mb = (b_band == bb)
    if not np.any(mb):
        continue
    for fb in range(5):
        mbf = mb & (f_band == fb)
        if not np.any(mbf):
            continue
        order = np.argsort(sizes_px[mbf])  # small→large reduces cover-up
        fig.add_trace(go.Scattergeo(
            lat=lat[mbf][order], lon=lon[mbf][order], mode="markers",
            marker=dict(
                size=sizes_px[mbf][order],
                color=br_c[mbf][order],               # color by brightness
                coloraxis="coloraxis",
                line=dict(width=0),
                opacity=float(opacities[fb])          # opacity by FRP only
            ),
            customdata=np.c_[br_c[mbf][order], fr_c[mbf][order]],
            hovertemplate=("Lat %{lat:.2f}, Lon %{lon:.2f}<br>"
                           "Brightness %{customdata[0]:.1f} K<br>"
                           "FRP (MW, capped) %{customdata[1]:.1f}<extra></extra>"),
            showlegend=False
        ))

fig.update_layout(
    title="World Wildfire Data",
    geo=dict(projection_type="natural earth", showcountries=True, showland=True),
    margin=dict(l=0, r=0, t=40, b=60),
    coloraxis=dict(
        colorscale="Inferno",
        cmin=300, cmax=450,
        colorbar=dict(
            title="Intensity",
            tickvals=[300, 350, 400, 450],
            ticktext=["Low", "Medium", "High", "Extreme"],
            len=0.75, thickness=20
        )
    )
)

fig.show()
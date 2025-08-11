# 16.6 - Refactoring:
from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert it to a Python object.
path = Path('../earthquake_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('../earthquake_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# Exercise 16-6: Refactor the for loop to list comprehensions.
mags = [eq_dicts['properties']['mag'] for eq_dicts in all_eq_dicts]
lons = [eq_dicts['geometry']['coordinates'][0] for eq_dicts in all_eq_dicts]
lats = [eq_dicts['geometry']['coordinates'][1] for eq_dicts in all_eq_dicts]
eq_titles = [eq_dicts['properties']['title'] for eq_dicts in all_eq_dicts]

# Exercise 16-6: Automated Title - Pull the chart title from the metadata section of the geojson file.
title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
    color=mags,
    color_continuous_scale='magma',
    labels={'color':'Magnitude'},
    projection='natural earth',
    hover_name=eq_titles,
)
fig.show()
# 16.4 - Automatic Indexes
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# path = Path('../weather_data/sitka_weather_2021_simple.csv')
path = Path('../weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_index = header_row.index("DATE")
high_index = header_row.index("TMAX")
low_index = header_row.index("TMIN")
name_index = header_row.index("NAME")

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
place_name = ""
for row in reader:
    # Grab the station name,  if it's not already set.
    if not place_name:
        place_name = row[name_index]

    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for: {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = header_row[0]
ax.set_title(f"Daily High and Low Temperatures, 2021\n{place_name}", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

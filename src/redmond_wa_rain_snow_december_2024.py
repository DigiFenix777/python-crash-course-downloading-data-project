from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('../weather_data/redmond_wa_2024_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()
print(f"Lines: {lines}")
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, rain, rain amount, snow, and snow amount.
dates, rain_day, rain_amt, snow_day, snow_amt = [], [], [], [], []

for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    try:
        precip = int(row[10])
        precip_attr = int(row[11])
        precip_s = int(row[12])
        precip_s_attr = int(row[13])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rain_day.append(precip)
        rain_amt.append(precip_attr)
        snow_day.append(precip_s)
        snow_amt.append(precip_s_attr)

print(f"Dates: {dates}")
print(f"Rain day: {rain_day}")
print(f"Rain amt: {rain_amt}")
print(f"Snow day: {snow_day}")
print(f"Snow amt: {snow_amt}")

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(range(len(dates)))
ax.scatter(rain_day, rain_amt, color='blue', s=50, alpha=0.5, label="Rainy Days")
ax.scatter(snow_day, snow_amt, color='gray', s=50, alpha=0.5, label="Snowy Days")


# Format plot
title = "Daily Rain and Snow, December 2024\nRedmond, WA"
ax.set_title(title, fontsize=24)
ax.set_xlabel('Day of the Month', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (inches)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

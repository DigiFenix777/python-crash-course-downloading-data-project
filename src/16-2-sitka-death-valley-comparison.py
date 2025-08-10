# 16.2 - Sitka/Death Valley Comparison
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Path to Sitka CSV.
path_sitka = Path('../weather_data/sitka_weather_2021_simple.csv')
lines_sitka = path_sitka.read_text(encoding='utf-8').splitlines()

# Path to Death Valley CSV.
path_death_valley = Path('../weather_data/death_valley_2021_simple.csv')
lines_death_valley = path_death_valley.read_text(encoding='utf-8').splitlines()

# Read Sitka CSV.
reader_sitka = csv.reader(lines_sitka)
header_row = next(reader_sitka)
print("\nSitka:")

# Print Sitka Headers
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Read Death Valley CSV.
reader_dv = csv.reader(lines_death_valley)
header_row = next(reader_dv)
print("\nDeath Valley:")

# Print Death Valley Headers.
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract high temperatures - Sitka.
dates, sitka_highs = [], []
for row in reader_sitka:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    print(current_date)
    high = int(row[4])
    dates.append(current_date)
    sitka_highs.append(high)

# Extract dates and high temperatures - Death Valley.
death_valley_highs = []
for row in reader_dv:
    try:
        high = int(row[3])
    except ValueError:
        print(f"Problem high on {row}: {repr(row[3])}")
    else:
        death_valley_highs.append(high)

# Plot the high temperatures at each location.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, death_valley_highs, color='red')
ax.plot(dates, sitka_highs, color='aquamarine')
ax.fill_between(dates, death_valley_highs, sitka_highs, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily High Temperatures, Death Valley, CA - Sitka, AK", fontsize=24)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
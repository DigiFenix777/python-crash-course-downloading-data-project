# Exercise 16.1: Sitka Rainfall
from pathlib import Path
import csv
import matplotlib.pyplot as plt
import sys

DATA = Path("../data/weather_data/sitka_weather_2021_full.csv")
if not DATA.exists():
    sys.exit(
        "Missing data file: data/sitka_weather_2021_full.csv\n"
        "See data/README.md for download instructions."
    )

path = Path('../data/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract rainfall total per day.
rainfall = []
for row in reader:
    rain = float(row[5])
    rainfall.append(rain)

# Plot the daily rainfall.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(rainfall, color='aquamarine')

# Format plot.
ax.set_title("Daily Rainfall in Sitka, AK, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Rainfall (inches)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
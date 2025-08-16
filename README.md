# 🌍 Data Visualization with CSV, APIs, and GeoJSON  

## 🔑 Executive Summary  
This project showcases **Python for data analysis and visualization** in a way that directly supports cybersecurity workflows. While the exercises focus on CSV, JSON, and GeoJSON datasets (weather, earthquakes, wildfires), the same skills apply to security data such as:  

- Parsing and cleaning **log files**, vulnerability scan results, and breach datasets.  
- Accessing and processing **security APIs** (e.g., VirusTotal, HaveIBeenPwned, Shodan).  
- Building **visualizations of attack trends** to communicate risks to stakeholders.  
- Applying **refactoring and error handling** that mirror practices in secure coding.  

👉 Recruiters and hiring managers: This project demonstrates my ability to work with real-world data and lays the groundwork for **automation and analysis in cybersecurity contexts**.   

---

## 📌 Overview  

This project demonstrates how to **ingest, process, and visualize structured and unstructured data** using Python. It includes:  

- Parsing and plotting weather data from CSV files.  
- Downloading JSON/GeoJSON datasets (earthquakes, wildfires).  
- Applying data cleaning, error checking, and refactoring.  
- Generating visualizations with **Matplotlib** amd **Plotly**, including static and interactive charts.  

---

## 🧠 Skills & Concepts  

- Data parsing from **CSV, JSON, and GeoJSON**  
- Dataset exploration  
- Time-series visualization with **datetime**  
- Plot customization (colors, scales, shading)  
- Global data mapping (earthquakes, fires)  
- Refactoring with list comprehensions and automated headers  
- Professional Git/GitHub workflow (branching, version control, `.gitignore`)  

---

## 🗂️ Repository Structure  

```plaintext
project-data-visualization/
│
├── src/                # Python scripts for each exercise
│   ├── 16_1_death_valley_rainfall.py
│   ├── 16_1_sitka_rainfall.py
│   ├── 16_2_sitka_death_valley_comparison.py
│   ├── 16_4_automatic_indexes.py
│   ├── 16_6_refactoring.py
│   ├── 16_7_automated_title.py
│   ├── 16_8_recent_earthquakes.py
│   ├── 16_9_world_fires.py
│   ├── death_valley_highs_lows.py
│   ├── eq_explore_data.py
│   ├── main.py
│   ├── redmond_wa_rain_snow_december_2024.py
│   ├── sitka_highs.py
│   └── sitka_highs_lows.py
│ 
├── data/               # Input CSV/JSON datasets
├── images/             # Exported static plots
├── html/               # Interactive Plotly charts
│
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```
---

## 🚀 How to Run  

1. Clone this repo and move into the folder:  
   ```bash
   git clone git@github.com:your-username/project-data-visualization.git
   cd project-data-visualization
   ```

2. (Optional) Create a virtual environment:
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

3. Install dependencies:
	```bash
	pip install -r requirements.txt
	```

4. Run any exercise script, for example:
	```bash
	python src/16_8_recent_earthquakes.py
	```

---
## 🔎 Skills Spotlight  

This project highlights skills in:  
- Python scripting for data processing  
- API and JSON handling with `requests`  
- Data visualization using **Matplotlib** and **Plotly**  
- Working with real-world datasets (climate, seismic, fire activity)  
- Applying **PEP 8**, project structuring, and GitHub portfolio practices  



---
## 📝 Lessons Learned  
Through this project, I strengthened both my Python skills and their application to cybersecurity:  

- **Data parsing & cleaning** → transferable to analyzing log files, firewall exports, and SIEM data.  
- **Datetime handling** → useful for correlating events across multiple security data sources.  
- **Visualization (Matplotlib & Plotly)** → critical for reporting incidents and trends to executives or compliance auditors.  
- **Error handling & validation** → aligns with defensive programming principles in security tools.  
- **Refactoring & automation** → prepares me to build reusable scripts for common security workflows.  

This project helped me bridge **Python fundamentals** with **practical cybersecurity applications**, positioning me to develop tools that improve detection, response, and reporting.  

___
## 📊 Exercises Implemented  

- **16-1: Sitka Rainfall** → Visualized daily rainfall (Sitka & Death Valley).  
- **16-2: Sitka–Death Valley Comparison** → Standardized y-axes for temperature comparisons.  
- **16-4: Automatic Indexes** → Automated detection of CSV header indexes and titles.  
- **16-6: Refactoring** → Simplified earthquake data parsing with list comprehensions.  
- **16-7: Automated Title** → Dynamically pulled dataset titles from GeoJSON metadata.  
- **16-8: Recent Earthquakes** → Visualized past 30 days of earthquake data (incl. 2025 Kamchatka quake).  
- **16-9: World Fires** → Plotted NASA FIRMS fire data with intensity-based opacity and color scaling.  


---
## 🌍 Data Sources  

- **NOAA Climate Data** — temperature and rainfall data for Sitka, Alaska, and Death Valley, California. [ncdc.noaa.gov](https://www.ncdc.noaa.gov/cdo-web) 
- **USGS Earthquake Hazards Program** — real-time and historical earthquake data in GeoJSON format: [earthquake.usgs.gov](https://earthquake.usgs.gov/earthquakes/feed)  
- **NASA Earthdata (FIRMS)** — global active fire data: [earthdata.nasa.gov/firms](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data)  
- Datasets and exercises adapted from *Python Crash Course, 3rd Edition* by Eric Matthes (No Starch Press).

---
## 📚 Attribution  

Based on exercises from:  
Matthes, E. (2023). *Python Crash Course* (3rd ed.). No Starch Press.  
[Book website](https://ehmatthes.github.io/pcc_3e/)  

---

## 🧩 License  

Distributed under the MIT License.  
See LICENSE for details.  
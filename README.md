# Chapter 16 – Downloading Data  
Projects and exercises from *Python Crash Course*, 3rd Edition by Eric Matthes  
📘 Focus: Reading data from APIs and CSV files, processing it, and visualizing the results.

---

## 📌 Overview

This repository contains the completed code and exercises from **Chapter 16: Downloading Data** of the book *Python Crash Course* (3rd Edition). This chapter explores how to fetch data from online sources and local files, process it using Python, and generate meaningful visualizations using Matplotlib and Plotly.

---

## 🧠 Key Concepts & Skills

- Reading and parsing **CSV** files with Python's `csv` module
- Using the **`requests`** library to access online APIs
- Processing **JSON** responses
- Visualizing data with **Matplotlib** and **Plotly**
- Handling real-world data such as temperatures, earthquakes, and more

---

## 🗂️ Project Structure

```plaintext
chapter-16-downloading-data/
│
├── src/                # Core Python scripts
│   └── main.py
│
├── data/               # Input CSV and JSON data
├── images/             # Exported static charts and plots
├── html/               # Interactive Plotly charts
├── notebooks/          # Optional Jupyter notebooks
├── tests/              # Unit tests (optional)
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── .venv/              # Virtual environment (not tracked in Git)
```

## 🚀 How to Run This Project
1. Clone the repo and cd into the folder:

```bash
git clone https://github.com/your-username/chapter-16-downloading-data.git
cd chapter-16-downloading-data
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
4. Run the program(s):
```bash 
python src/main.py
```
## 📚 Attribution
This project is based on exercises and examples from:

Matthes, E. (2023). Python Crash Course (3rd ed.). No Starch Press.
https://ehmatthes.github.io/pcc_3e/

## 🧩 License
Distributed under the MIT License.
See LICENSE for more information.
=# US Traffic Accidents Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project performs an Exploratory Data Analysis (EDA) on a massive country-wide dataset of US traffic accidents spanning from 2016 to 2023. The goal of this analysis is to identify key safety patterns, including high-risk accident hours, weekly patterns, leading weather contributing factors, and critical geographical accident hotspots.

By uncovering these patterns, this project demonstrates how data-driven insights can highlight high-risk periods and locations to assist in traffic management and accident prevention strategies.

---

## 📊 Key Insights & Analysis

### 1. Temporal Analysis (Time & Day Patterns)
* **Rush Hour Spikes:** Accidents peak dramatically on weekdays during the morning rush hours (**7:00 AM – 9:00 AM**) and evening rush hours (**4:00 PM – 6:00 PM**). This points directly to a heavy correlation with high commuter volume and traffic congestion.
* **Weekend Distribution:** On Saturdays and Sundays, the sharp rush-hour spikes disappear, replacing them with a much flatter, evenly distributed curve that peaks in the afternoon. Total accident counts are also noticeably lower on weekends.

### 2. Environmental & Weather Factors
* **Clear Weather Paradox:** The data reveals that the highest total number of accidents occurs during "Clear" or "Fair" weather conditions. 
* **The Insight:** While severe weather (rain, fog, snow) increases driving difficulty, the sheer volume of drivers on the road during clear days—combined with speed and driver distraction—results in a higher overall frequency of incidents.

### 3. Geospatial Hotspots
* **Urban Clusters:** By filtering and mapping coordination data (Latitude/Longitude) for high-density regions like California, the visualization shows tight clusters localized heavily around major highway junctions, highway interchanges, and entry/exit ramps where lane-merging behavior is frequent.

---

## 🖼️ Visualizations

### 1. Accident Frequency by Hour and Day
This chart visualizes the distribution of traffic incidents across the 24-hour cycle and contrasts weekday commute spikes against weekend leisure travel.
![Time Analysis](time_analysis.png)

### 2. Top Contributing Weather Conditions
This breakdown highlights the top 10 weather environments documented at the time and location of the recorded traffic accidents.
![Weather Analysis](weather_analysis.png)

---

## 🗺️ Interactive Geospatial Map
The project generates an interactive, browser-based map using a Folium HeatMap plugin. 
* **File:** `accident_hotspots_map.html`
* **How to view it:** Download the HTML file from this repository and double-click it. It will open in your default web browser, allowing you to zoom in and out of high-density metropolitan corridors to explore accident clusters interactively.

---

## 🛠️ Technologies & Libraries Used
* **Python 3.11**
* **Pandas** – For efficient data ingestion, subsetting columns, handling missing values, and datetime parsing.
* **NumPy** – For structural vector arrays and mathematical operations.
* **Matplotlib & Seaborn** – For crafting the comparative statistical plots and count distributions.
* **Folium** – For handling coordinate geometry and building the dynamic HTML heatmap layer.

---

## 📂 Dataset Reference
The data utilized in this repository is sourced from the **US Accidents (2016 - 2023)** dataset available on Kaggle. 
* *Note: The raw CSV file (`US_Accidents_March23.csv`) contains millions of rows and exceeds GitHub's 100MB file limit; therefore, it has been omitted from this repository. You can download the source file directly from Kaggle to run the script locally.*

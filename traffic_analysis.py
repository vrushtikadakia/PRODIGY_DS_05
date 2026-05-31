import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# 1. LOAD DATA
print("1/5: Loading dataset... This will take a moment.")
columns_needed = [
    'Severity', 'Start_Time', 'Start_Lat', 'Start_Lng', 
    'State', 'Weather_Condition', 'Crossing', 'Junction', 
    'Traffic_Signal'
]
df = pd.read_csv('US_Accidents_March23.csv', usecols=columns_needed)
print(f"Successfully loaded {len(df):,} rows.")

# 2. CLEAN & PREPARE DATA
print("2/5: Cleaning data and extracting time features...")
df.dropna(subset=['Start_Time', 'Start_Lat', 'Start_Lng', 'Weather_Condition'], inplace=True)
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df.dropna(subset=['Start_Time'], inplace=True)

df['Hour'] = df['Start_Time'].dt.hour
df['Day_of_Week'] = df['Start_Time'].dt.day_name()

# 3. GENERATE CHARTS (Time & Day)
print("3/5: Generating time and day charts...")
plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.countplot(data=df, x='Hour', palette='viridis')
plt.title('Accident Frequency by Hour of the Day')
plt.xlabel('Hour of Day (0-23)')
plt.ylabel('Number of Accidents')

plt.subplot(1, 2, 2)
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(data=df, x='Day_of_Week', order=day_order, palette='magma')
plt.title('Accident Frequency by Day of the Week')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. GENERATE WEATHER CHART
print("4/5: Generating weather condition chart...")
plt.figure(figsize=(10, 5))
top_weather = df['Weather_Condition'].value_counts().head(10)
sns.barplot(x=top_weather.values, y=top_weather.index, palette='Blues_r')
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Number of Accidents')
plt.tight_layout()
plt.show()

# 5. GENERATE GEOSPATIAL MAP
print("5/5: Generating interactive hotspot map for California...")
map_df = df[df['State'] == 'CA'].sample(n=5000, random_state=42)
map_center = [map_df['Start_Lat'].mean(), map_df['Start_Lng'].mean()]
m = folium.Map(location=map_center, zoom_start=6, tiles='CartoDB positron')
heat_data = map_df[['Start_Lat', 'Start_Lng']].values.tolist()
HeatMap(heat_data, radius=12, max_zoom=10).add_to(m)
m.save("accident_hotspots_map.html")

print("\nTask complete! The interactive map has been saved as 'accident_hotspots_map.html' in your folder.")
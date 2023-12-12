import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from api import const_api

area_url = const_api.areas_url
crime_desc_url = const_api.crime_desc_url

response_area = requests.get(area_url)
areas_data = response_area.json()

response_crimes = requests.get(crime_desc_url)
crime_data = response_crimes.json()


df_crime = pd.DataFrame(crime_data['crime_descriptions'], columns=['dr_no', 'crm_cd_desc'])
df_areas = pd.DataFrame(areas_data['areas'], columns=['dr_no', 'area', 'area_name'])

df_merged = pd.merge(df_crime, df_areas, on='dr_no')

crime_counts = df_merged.groupby(['area_name', 'crm_cd_desc']).size().unstack(fill_value=0)

plt.figure(figsize=(15, 10))
sns.heatmap(crime_counts, cmap='YlGnBu', annot=True, fmt='g', cbar_kws={'label': 'Crime Count'})
plt.title('Distribution of Crimes in Each Area')
plt.xlabel('Crime Code Description')
plt.ylabel('Area Name')
plt.xticks(rotation=20, ha='right')
plt.yticks(fontsize=10)
plt.show()


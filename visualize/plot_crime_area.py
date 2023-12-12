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

df_crime = pd.DataFrame(crime_data['crime_descriptions'], columns=['crm_cd_desc', 'crm_cd', 'dr_no'])
df_areas = pd.DataFrame(areas_data['areas'], columns=['area', 'rpt_dist_no', 'area_name', 'dr_no'])

# Merging DataFrames on 'dr_no'
df_merged = pd.merge(df_crime, df_areas, on='dr_no')
all_areas = df_areas['area'].unique()
all_crime_descs = df_crime['crm_cd_desc'].unique()
# Counting the occurrences of crimes in each area

crime_counts = df_merged.groupby('area')['crm_cd_desc'].value_counts().unstack().fillna(0)

# Plotting the distribution of crimes in each area
plt.figure(figsize=(15, 8))
sns.heatmap(crime_counts, cmap='YlGnBu', annot=True, fmt='g', cbar_kws={'label': 'Crime Count'})
plt.title('Distribution of Crimes in Each Area')
plt.xlabel('Crime Code Description')
plt.ylabel('Area')
plt.xticks(rotation=10, ha='right')  # Rotate x-axis labels for better visibility
plt.show()


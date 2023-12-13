import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from api import const_api

victim_url = const_api.victims_url
crime_description_url = const_api.crime_desc_url
area_url = const_api.areas_url

response_victim = requests.get(victim_url)
response_crime_description = requests.get(crime_description_url)
response_area = requests.get(area_url)

victim_data = response_victim.json()
crime_description_data = response_crime_description.json()
area_data = response_area.json()

df_victim = pd.DataFrame(victim_data['victims'], columns=['dr_no', 'vict_sex'])
df_crime_description = pd.DataFrame(crime_description_data['crime_descriptions'], columns=['dr_no', 'crm_cd_desc'])
df_area = pd.DataFrame(area_data['areas'], columns=['dr_no', 'rpt_dist_no'])

df_merged = pd.merge(df_victim, df_crime_description, on='dr_no')
df_merged = pd.merge(df_merged, df_area, on='dr_no')

selected_crime_desc = df_merged['crm_cd_desc'].value_counts().nlargest(10).index
df_merged_subset = df_merged[df_merged['crm_cd_desc'].isin(selected_crime_desc)]

df_merged_subset['count'] = 1

plt.figure(figsize=(15, 8))
ax = sns.countplot(data=df_merged_subset, x='rpt_dist_no', hue='vict_sex', hue_order=['M', 'F', 'X'], palette='Set1')
plt.title("Distribution of Reporting District by Victim's Sex and Crime Count")
plt.xlabel('Reporting District')
plt.ylabel('Number Of Crimes')
plt.legend(title='Victim Sex', loc='upper right')
plt.xticks(rotation=45, ha='right')

plt.show()

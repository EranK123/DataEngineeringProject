import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from api import const_api

victim_url = const_api.victims_url
weapon_url = const_api.weapons_url

response_victim = requests.get(victim_url)
victim_data = response_victim.json()

response_weapon = requests.get(weapon_url)
weapon_data = response_weapon.json()

df_victim = pd.DataFrame(victim_data['victims'], columns=['dr_no', 'vict_sex'])
df_weapon = pd.DataFrame(weapon_data['weapons'], columns=['dr_no', 'weapon_desc'])

df_merged = pd.merge(df_victim, df_weapon, on='dr_no')
df_merged['weapon_desc'].fillna('Unknown', inplace=True)
print(df_merged)

victim_sex_counts = df_merged.groupby(['weapon_desc', 'vict_sex']).size().unstack(fill_value=0)

df_merged['count'] = 1

# Create a bar plot for the distribution of victim sex for each weapon
plt.figure(figsize=(15, 8))
sns.countplot(data=df_merged, x='weapon_desc', hue='vict_sex')
plt.title('Distribution of Victim Sex for Each Weapon')
plt.xlabel('Weapon Description')
plt.ylabel('Count')
plt.legend(title='Victim Sex')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.show()
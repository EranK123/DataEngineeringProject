import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from api import const_api

api_url = const_api.weapons_url

response = requests.get(api_url)
data = response.json()
df_weapons = pd.DataFrame(data['weapons'], columns=['weapon_used_cd', 'weapon_desc'])

weapon_codes = df_weapons['weapon_used_cd']
weapon_descs = df_weapons['weapon_desc']

plt.figure(figsize=(12, 6))
sns.countplot(x=weapon_codes, palette='bright')
plt.title('Count of Weapon Codes')
plt.xlabel('Weapon Code')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(weapon_codes, weapon_descs, color='orange')
plt.title('Distribution between Weapon Codes and Descriptions')
plt.xlabel('Weapon Code')
plt.ylabel('Weapon Description')

for i, code in enumerate(weapon_codes):
    plt.annotate(code, (weapon_codes[i], weapon_descs[i]), textcoords="offset points", xytext=(0, 5), ha='center')

plt.tight_layout()
plt.show()

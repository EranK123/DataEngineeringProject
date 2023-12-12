import requests
import matplotlib.pyplot as plt
import seaborn as sns
from api import const

api_url = const.weapons_url

response = requests.get(api_url)
data = response.json()

weapon_codes = [entry['weapon_used_cd'] for entry in data['weapons']]
weapon_descs = [entry['weapon_desc'] for entry in data['weapons']]

# Countplot for weapon codes
plt.figure(figsize=(12, 6))
sns.countplot(x=weapon_codes, palette='bright')
plt.title('Count of Weapon Codes')
plt.xlabel('Weapon Code')
plt.ylabel('Count')
plt.show()

# Scatter plot for distribution between weapon codes and descriptions
plt.figure(figsize=(12, 6))
plt.scatter(weapon_codes, weapon_descs, color='orange')
plt.title('Distribution between Weapon Codes and Descriptions')
plt.xlabel('Weapon Code')
plt.ylabel('Weapon Description')

for i, code in enumerate(weapon_codes):
    plt.annotate(code, (weapon_codes[i], weapon_descs[i]), textcoords="offset points", xytext=(0, 5), ha='center')

plt.tight_layout()
plt.show()

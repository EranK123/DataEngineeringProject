import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sb
from api import const

api_url = const.crimes_url

response = requests.get(api_url)
data = response.json()

crime_names = [entry['crm_cd_desc'] for entry in data['crime_descriptions']]
crime_codes = [entry['crm_cd'] for entry in data['crime_descriptions']]

plt.figure(figsize=(12, 6))
plt.scatter(crime_codes, crime_names, color='skyblue')
plt.title('Crime Code to Crime Name')
plt.xlabel('Crime Code')
plt.ylabel('Crime Name')

for i, code in enumerate(crime_codes):
    plt.annotate(code, (crime_codes[i], crime_names[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.figure(figsize=(12, 6))
sb.countplot(y=crime_names, order=pd.value_counts(crime_names).index, palette='viridis')
plt.title('Count of Each Crime Name')
plt.xlabel('Count')
plt.ylabel('Crime Name')

plt.tight_layout()
plt.show()

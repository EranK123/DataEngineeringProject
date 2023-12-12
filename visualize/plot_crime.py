import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sb
from api import const_api

api_url = const_api.crime_desc_url

response = requests.get(api_url)
data = response.json()

df_crimes = pd.DataFrame(data['crime_descriptions'], columns=['crm_cd_desc', 'crm_cd'])
crime_names = df_crimes['crm_cd_desc']
crime_codes = df_crimes['crm_cd']

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

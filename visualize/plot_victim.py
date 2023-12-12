import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sb
from api import const_api

api_url = const_api.victims_url

response = requests.get(api_url)
data = response.json()

df_victims = pd.DataFrame(data['victims'], columns=['vict_age', 'vict_sex', 'vict_descent'])

victim_ages = df_victims['vict_age']
victim_sexes = df_victims['vict_sex']
victim_descents = df_victims['vict_descent']

plt.figure(figsize=(12, 6))
sb.countplot(x=victim_ages, palette='muted')
plt.title('Count of Victim Ages')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 6))
sb.countplot(x=victim_sexes, palette='pastel')
plt.title('Count of Victim Sexes')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(12, 6))
sb.countplot(x=victim_descents, palette='dark')
plt.title('Count of Victim Descents')
plt.xlabel('Descent')
plt.ylabel('Count')
plt.show()

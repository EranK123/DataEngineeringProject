import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sb
from api import const

api_url = const.victims_url

response = requests.get(api_url)
data = response.json()

victim_ages = [entry['vict_age'] for entry in data['victims']]
victim_sexes = [entry['vict_sex'] for entry in data['victims']]
victim_descents = [entry['vict_descent'] for entry in data['victims']]

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

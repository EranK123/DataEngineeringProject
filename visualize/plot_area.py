import pandas as pd
import requests
import matplotlib.pyplot as plt
from api import const_api

api_url = const_api.areas_url
response = requests.get(api_url)
data = response.json()

df = pd.DataFrame(data['areas'], columns=['area', 'rpt_dist_no', 'area_name'])
areas = df['area']
rpt_dist_nos = df['rpt_dist_no']
area_names = df['area_name']


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(areas, rpt_dist_nos, color='blue')
plt.title('Area Number vs Reporting District')
plt.xlabel('Area Code')
plt.ylabel('District Number')

plt.subplot(1, 2, 2)
plt.scatter(area_names, areas, color='green')
plt.title('Area Name vs Area Number')
plt.xlabel('Area Name')
plt.ylabel('Area Code')

plt.tight_layout()
plt.show()

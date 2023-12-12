import requests
import matplotlib.pyplot as plt
from api import const
api_url = const.areas_url

response = requests.get(api_url)
data = response.json()


areas = [entry['area'] for entry in data['areas']]
rpt_dist_nos = [entry['rpt_dist_no'] for entry in data['areas']]
area_names = [entry['area_name'] for entry in data['areas']]


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

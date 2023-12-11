import matplotlib.pyplot as plt
from DataHandeling.DatabaseHandler import DatabaseHandler

db_handler = DatabaseHandler('CRIMES')
db_handler.cursor.execute("SELECT AREA, AREA_NAME, Rpt_Dist_No FROM area")

rows = db_handler.cursor.fetchall()
area = [row[0] for row in rows]
area_name = [row[1] for row in rows]
rpt_dist_no = [row[2] for row in rows]

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(area, rpt_dist_no, color='blue')
plt.title('Area Number vs Reporting District')
plt.xlabel('Area Code')
plt.ylabel('District Number')

plt.subplot(1, 2, 2)
plt.scatter(area_name, area, color='green')
plt.title('Area Name vs Area Number')
plt.xlabel('Area Name')
plt.ylabel('Area Code')

plt.tight_layout()
plt.show()
db_handler.close_connection()

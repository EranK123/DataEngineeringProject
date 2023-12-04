import matplotlib.pyplot as plt
from DatabaseHandler import DatabaseHandler

db_handler = DatabaseHandler('CRIMES')

db_handler.cursor.execute("SELECT weapon_used_cd, weapon_desc FROM weapon")
rows = db_handler.cursor.fetchall()
weapon_used_cd = [row[0] for row in rows if row[0] is not None]
weapon_desc = [row[1] for row in rows if row[1] is not None]

plt.figure(figsize=(12, 6))
plt.scatter(weapon_used_cd, weapon_desc, color='skyblue')
plt.title('Weapon Code to Description')
plt.xlabel('Weapon Code')
plt.ylabel('Weapon Description')

for i, txt in enumerate(weapon_used_cd):
    plt.annotate(txt, (weapon_used_cd[i], weapon_desc[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
db_handler.close_connection()
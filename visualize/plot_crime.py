import matplotlib.pyplot as plt
import seaborn as sb
from DatabaseHandler import DatabaseHandler

db_handler = DatabaseHandler('CRIMES')
db_handler.cursor.execute("SELECT crm_cd, crm_cd_desc FROM crime_description")

rows = db_handler.cursor.fetchall()
print(rows)
crime_codes = [row[0] for row in rows if row[0] is not None]
print(crime_codes)
crime_names = [row[1] for row in rows if row[1] is not None]

plt.figure(figsize=(12, 6))
plt.scatter(crime_codes, crime_names, color='skyblue')
plt.title('Crime Code to Crime Name')
plt.xlabel('Crime Code')
plt.ylabel('Crime Name')

for i, code in enumerate(crime_codes):
    plt.annotate(code, (crime_codes[i], crime_names[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.figure(figsize=(12, 6))
sb.countplot(y=crime_names, palette='viridis')
plt.title('Count of Each Crime')
plt.xlabel('Count')
plt.ylabel('Crime Name')

plt.tight_layout()
plt.show()

db_handler.close_connection()

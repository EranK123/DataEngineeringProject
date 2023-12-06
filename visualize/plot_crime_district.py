import matplotlib.pyplot as plt
import seaborn as sns
from DatabaseHandler import DatabaseHandler

db_handler = DatabaseHandler('CRIMES')

db_handler.cursor.execute("SELECT a.Rpt_Dist_No, cd.crm_cd FROM area a JOIN crime_description cd ON a.row_num = cd.row_num")
rows = db_handler.cursor.fetchall()
print(rows)

districts = [row[0] for row in rows if row[0] is not None]
crime_codes = [row[1] for row in rows if row[1] is not None]

plt.figure(figsize=(12, 6))
sns.countplot(x=districts, palette='viridis')
plt.title('Distribution of Crimes by District')
plt.xlabel('District')
plt.ylabel('Count of Crimes')

plt.tight_layout()
plt.show()

db_handler.close_connection()

import matplotlib.pyplot as plt
import seaborn as sns

from DatabaseHandler import DatabaseHandler

db_handler = DatabaseHandler('CRIMES')

db_handler.cursor.execute("SELECT vict_age, vict_sex, vict_descent FROM victim")

rows = db_handler.cursor.fetchall()

vict_age = [row[0] for row in rows]
vict_sex = [row[1] for row in rows]
vict_descent = [row[2] for row in rows]

plt.figure(figsize=(16, 8))

plt.subplot(2, 2, 1)
sns.countplot(x=vict_age, palette='viridis')
plt.title('Count of Ages')

plt.subplot(2, 2, 2)
sns.countplot(x=vict_sex, palette='muted')
plt.title('Count of Sex')

plt.subplot(2, 2, 3)
sns.countplot(x=vict_descent, palette='pastel')
plt.title('Count of Descent')

plt.tight_layout()
plt.show()

db_handler.close_connection()

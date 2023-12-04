import psycopg2
import time
from Pipeline import uploader
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(
    host=os.getenv('CRIMESLA_DB_HOST'),
    database=os.getenv('CRIMESLA_DB_DATABASE'),
    user=os.getenv('CRIMESLA_DB_USER'),
    password=os.getenv('CRIMESLA_DB_PASSWORD'),
    port=os.getenv('CRIMESLA_DB_PORT')
)

cursor = connection.cursor()
query = "SELECT * FROM allcrimedata;"
cursor.execute(query)


def read_entry():
    is_entry = True
    while is_entry:
        row = cursor.fetchone()
        if row:
            entry = dict(zip((column[0] for column in cursor.description), row))
            yield entry
            time.sleep(5)
        else:
            is_entry = False


for entry in read_entry():
    uploader.upload_to_crimes_db(entry)
cursor.close()
connection.close()

import os
import psycopg2
from dotenv import load_dotenv


class DatabaseHandler:
    def __init__(self, db_name):
        load_dotenv()

        self.crimes_connection = psycopg2.connect(
            host=os.getenv(f'{db_name}_DB_HOST'),
            database=os.getenv(f'{db_name}_DB_DATABASE'),
            user=os.getenv(f'{db_name}_DB_USER'),
            password=os.getenv(f'{db_name}_DB_PASSWORD'),
            port=os.getenv(f'{db_name}_DB_PORT')
        )

        self.cursor = self.crimes_connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.crimes_connection.close()

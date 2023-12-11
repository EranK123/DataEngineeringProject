import os
import psycopg2
from dotenv import load_dotenv
import const


class DatabaseHandler:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DatabaseHandler, cls).__new__(cls)
        return cls.__instance

    def __init__(self, db_name):
        load_dotenv()

        self.connection = psycopg2.connect(
            host=os.getenv(f'{db_name}_DB_HOST'),
            database=os.getenv(f'{db_name}_DB_DATABASE'),
            user=os.getenv(f'{db_name}_DB_USER'),
            password=os.getenv(f'{db_name}_DB_PASSWORD'),
            port=os.getenv(f'{db_name}_DB_PORT')
        )

        self.cursor = self.connection.cursor()
        self.query = const.ALL_CRIME_QUERY

    def insert(self, table_name, column_names, values):
        insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) " \
                       f"VALUES ({', '.join(['%s' for _ in values])});"
        self.cursor.execute(insert_query, values)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def get_column_names(self, table_name):
        query = const.ALL_TABLE_NAMES_QUERY
        self.cursor.execute(query, (table_name,))
        columns = [column[0] for column in self.cursor.fetchall()]
        return columns



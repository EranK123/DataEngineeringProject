import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import os

db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'Peach124',
    'port': 5432  # Replace with your PostgreSQL port if different
}

# Create a connection to the PostgreSQL server
conn = psycopg2.connect(
    host=db_params['host'],
    database=db_params['database'],
    user=db_params['user'],
    password=db_params['password'],
    port=db_params['port']
)

# Create a cursor object
cur = conn.cursor()

# Set automatic commit to be true
conn.set_session(autocommit=True)
# cur.execute("CREATE DATABASE IF NOT EXISTS CrimesLA")

conn.commit()
cur.close()
conn.close()

db_params['database'] = 'crimesla'
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')

csv_files = {
    'area': 'area.csv',
    'case': 'case.csv',
    'case_details': 'case_details.csv',
    'crime_description': 'crime_description.csv',
    'victim': 'victim.csv',
    'weapon': 'weapon.csv'
}
#
# for table_name, file_path in csv_files.items():
#     print(f"Contents of '{table_name}' CSV file:")
#     df = pd.read_csv(file_path)
#     print(df.head(2))
#     print("\n")

for table_name, file_path in csv_files.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)



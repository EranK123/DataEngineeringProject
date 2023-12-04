import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import os

db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'Peach124',
    'port': 5432
}

conn = psycopg2.connect(
    host=db_params['host'],
    database=db_params['database'],
    user=db_params['user'],
    password=db_params['password'],
    port=db_params['port']
)

cur = conn.cursor()
conn.set_session(autocommit=True)
# cur.execute("CREATE DATABASE IF NOT EXISTS CrimesLA")

conn.commit()
cur.close()
conn.close()

db_params['database'] = 'crimesla'
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')

crime_data_path = "/Users/erankatz/DataEngineeringProject/CrimeData.csv"


df = pd.read_csv(crime_data_path)
df.to_sql('allcrimedata', engine, if_exists='replace', index=False)


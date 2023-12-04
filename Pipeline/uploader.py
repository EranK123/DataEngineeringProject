import psycopg2
import logging
import os
from dotenv import load_dotenv


def insert(cursor, table_name, column_names, values):
    insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) " \
                   f"VALUES ({', '.join(['%s' for _ in values])});"
    cursor.execute(insert_query, values)
    logging.info(f"Inserted into {table_name} table")


def upload_to_crimes_db(entry):
    load_dotenv()
    crimes_connection = psycopg2.connect(
        host=os.getenv('CRIMES_DB_HOST'),
        database=os.getenv('CRIMES_DB_DATABASE'),
        user=os.getenv('CRIMES_DB_USER'),
        password=os.getenv('CRIMES_DB_PASSWORD'),
        port=os.getenv('CRIMES_DB_PORT')
    )

    crimes_cursor = crimes_connection.cursor()
    insert(crimes_cursor, 'area', ['AREA', 'AREA_NAME', 'Rpt_Dist_No'],
           [entry['AREA'], entry['AREA NAME'], entry['Rpt Dist No']])
    insert(crimes_cursor, 'crime_description', ['Crm_Cd', 'Crm_Cd_Desc'], [entry['Crm Cd'], entry['Crm Cd Desc']])
    insert(crimes_cursor, 'weapon', ['Weapon_Used_Cd', 'Weapon_Desc'], [entry['Weapon Used Cd'], entry['Weapon Desc']])
    insert(crimes_cursor, 'victim', ['VictId', 'Vict_Age', 'Vict_Sex', 'Vict_Descent'],
           [entry['VictId'], entry['Vict Age'], entry['Vict Sex'], entry['Vict Descent']])
    insert(crimes_cursor, 'case_details', ['DR_NO', 'DATE_OCC', 'TIME_OCC', 'Mocodes', 'LOCATION', 'LAT', 'LON'],
           [entry['DR_NO'], entry['DATE OCC'], entry['TIME OCC'],
            entry['Mocodes'], entry['LOCATION'], entry['LAT'],
            entry['LON']])
    insert(crimes_cursor, 'case_relation', ['DR_NO', 'VictId', 'AREA', 'Crm_Cd', 'Weapon_Used_Cd'],
           [entry['DR_NO'], entry['VictId'], entry['AREA'], entry['Crm Cd'], entry['Weapon Used Cd']])

    crimes_connection.commit()

    crimes_cursor.close()
    crimes_connection.close()

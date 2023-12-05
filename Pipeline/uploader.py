import logging
from DatabaseHandler import DatabaseHandler


def insert(cursor, table_name, column_names, values):
    insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) " \
                   f"VALUES ({', '.join(['%s' for _ in values])});"
    cursor.execute(insert_query, values)
    logging.info(f"Inserted into {table_name} table")


def upload_to_crimes_db(entry):
    db_handler = DatabaseHandler('CRIMES')
    insert(db_handler.cursor, 'area', ['AREA', 'AREA_NAME', 'Rpt_Dist_No'],
           [entry['AREA'], entry['AREA NAME'], entry['Rpt Dist No']])
    insert(db_handler.cursor, 'crime_description', ['Crm_Cd', 'Crm_Cd_Desc'], [entry['Crm Cd'], entry['Crm Cd Desc']])
    insert(db_handler.cursor, 'weapon', ['Weapon_Used_Cd', 'Weapon_Desc'], [entry['Weapon Used Cd'], entry['Weapon Desc']])
    insert(db_handler.cursor, 'victim', ['VictId', 'Vict_Age', 'Vict_Sex', 'Vict_Descent'],
           [entry['VictId'], entry['Vict Age'], entry['Vict Sex'], entry['Vict Descent']])
    insert(db_handler.cursor, 'case_details', ['DR_NO', 'DATE_OCC', 'TIME_OCC', 'Mocodes', 'LOCATION', 'LAT', 'LON'],
           [entry['DR_NO'], entry['DATE OCC'], entry['TIME OCC'],
            entry['Mocodes'], entry['LOCATION'], entry['LAT'],
            entry['LON']])
    insert(db_handler.cursor, 'case_relation', ['DR_NO', 'VictId', 'AREA', 'Crm_Cd', 'Weapon_Used_Cd'],
           [entry['DR_NO'], entry['VictId'], entry['AREA'], entry['Crm Cd'], entry['Weapon Used Cd']])


    db_handler.crimes_connection.commit()
    db_handler.close_connection()

import psycopg2
import logging


def upload_area(cursor, area_data):
    insert_query = "INSERT INTO area (AREA, AREA_NAME, Rpt_Dist_No) VALUES (%s, %s, %s);"
    cursor.execute(insert_query, (area_data['AREA'], area_data['AREA NAME'], area_data['Rpt Dist No']))
    logging.info("Inserted to area table")


def upload_crime_description(cursor, crime_description_data):
    insert_query = "INSERT INTO crime_description (Crm_Cd, Crm_Cd_Desc) VALUES (%s, %s);"
    cursor.execute(insert_query, (crime_description_data['Crm Cd'], crime_description_data['Crm Cd Desc']))
    logging.info("Inserted to crime_description table")


def upload_weapon(cursor, weapon_data):
    insert_query = "INSERT INTO weapon (Weapon_Used_Cd, Weapon_Desc) VALUES (%s, %s);"
    cursor.execute(insert_query, (weapon_data['Weapon Used Cd'], weapon_data['Weapon Desc']))
    logging.info("Inserted to weapon table")


def upload_victim(cursor, victim_data):
    insert_query = "INSERT INTO victim (VictId, Vict_Age, Vict_Sex, Vict_Descent) VALUES (%s, %s, %s, %s);"
    cursor.execute(insert_query, (
        victim_data['VictId'], victim_data['Vict Age'], victim_data['Vict Sex'], victim_data['Vict Descent']))
    logging.info("Inserted to victim table")


def upload_case_details(cursor, case_details_data):
    insert_query = "INSERT INTO case_details (DR_NO, DATE_OCC, TIME_OCC, Mocodes, LOCATION, LAT, LON) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(insert_query, (
        case_details_data['DR_NO'], case_details_data['DATE OCC'], case_details_data['TIME OCC'],
        case_details_data['Mocodes'], case_details_data['LOCATION'], case_details_data['LAT'],
        case_details_data['LON']))
    logging.info("Inserted to case_details table")


def upload_case(cursor, case_data):
    insert_query = "INSERT INTO case_relation (DR_NO, VictId, AREA, Crm_Cd, Weapon_Used_Cd) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(insert_query, (
        case_data['DR_NO'], case_data['VictId'], case_data['AREA'], case_data['Crm Cd'], case_data['Weapon Used Cd']))
    logging.info("Inserted to case_relation table")


def upload_to_crimes_db(entry):
    crimes_db_params = {
        'host': 'localhost',
        'database': 'crimes',
        'user': 'postgres',
        'password': 'Peach124',
        'port': 5432
    }

    crimes_connection = psycopg2.connect(
        host=crimes_db_params['host'],
        database=crimes_db_params['database'],
        user=crimes_db_params['user'],
        password=crimes_db_params['password'],
        port=crimes_db_params['port']
    )

    crimes_cursor = crimes_connection.cursor()

    upload_area(crimes_cursor, entry)
    upload_crime_description(crimes_cursor, entry)
    upload_weapon(crimes_cursor, entry)
    upload_victim(crimes_cursor, entry)
    upload_case_details(crimes_cursor, entry)
    upload_case(crimes_cursor, entry)

    crimes_connection.commit()

    crimes_cursor.close()
    crimes_connection.close()

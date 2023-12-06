from DatabaseHandler import DatabaseHandler
import const


def upload_to_crimes_db(entry):
    db_handler = DatabaseHandler(const.SPLITED_CRIME_DBNAME)
    db_handler.insert('area', ['AREA', 'AREA_NAME', 'Rpt_Dist_No'],
                      [entry['AREA'], entry['AREA NAME'], entry['Rpt Dist No']])
    db_handler.insert('crime_description', ['Crm_Cd', 'Crm_Cd_Desc'], [entry['Crm Cd'], entry['Crm Cd Desc']])
    db_handler.insert('weapon', ['Weapon_Used_Cd', 'Weapon_Desc'],
                      [entry['Weapon Used Cd'], entry['Weapon Desc']])
    db_handler.insert('victim', ['VictId', 'Vict_Age', 'Vict_Sex', 'Vict_Descent'],
                      [entry['VictId'], entry['Vict Age'], entry['Vict Sex'], entry['Vict Descent']])
    db_handler.insert('case_details', ['DR_NO', 'DATE_OCC', 'TIME_OCC', 'Mocodes', 'LOCATION', 'LAT', 'LON'],
                      [entry['DR_NO'], entry['DATE OCC'], entry['TIME OCC'],
                       entry['Mocodes'], entry['LOCATION'], entry['LAT'],
                       entry['LON']])
    db_handler.insert('case_relation', ['DR_NO', 'VictId', 'AREA', 'Crm_Cd', 'Weapon_Used_Cd'],
                      [entry['DR_NO'], entry['VictId'], entry['AREA'], entry['Crm Cd'], entry['Weapon Used Cd']])

    db_handler.connection.commit()
    db_handler.close_connection()

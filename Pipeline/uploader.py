from DatabaseHandler import DatabaseHandler
import const


def upload_to_crimes_db(entry):
    db_handler = DatabaseHandler(const.SPLITED_CRIME_DBNAME)
    db_handler.insert(const.TABLE_NAMES['area'], const.AREA_TABLE_NAMES,
                      [entry[col.replace('_', ' ')] for col in const.AREA_TABLE_NAMES])

    db_handler.insert(const.TABLE_NAMES['crime_description'], const.CRIME_TABLE_NAMES,
                      [entry[col.replace('_', ' ')] for col in const.CRIME_TABLE_NAMES])

    db_handler.insert(const.TABLE_NAMES['weapon'], const.WEAPON_TABLE_NAMES,
                      [entry[col.replace('_', ' ')] for col in const.WEAPON_TABLE_NAMES])

    db_handler.insert(const.TABLE_NAMES['victim'], const.VICTIM_TABLE_NAMES,
                      [entry[col.replace('_', ' ')] for col in const.VICTIM_TABLE_NAMES])

    db_handler.insert(const.TABLE_NAMES['case_details'], const.CASE_DETS_TABLE_NAMES,
                      [entry[const.CASE_DETS_TABLE_NAMES[0]]] + [entry[col.replace('_', ' ')] for col in const.CASE_DETS_TABLE_NAMES[1:]])

    db_handler.insert(const.TABLE_NAMES['case_relation'], const.CASE_RELATION_TABLE_NAMES,
                      [entry[const.CASE_RELATION_TABLE_NAMES[0]]] + [entry[col.replace('_', ' ')] for col in const.CASE_RELATION_TABLE_NAMES[1:]])

    db_handler.connection.commit()
    db_handler.close_connection()

import psycopg2
import time

db_params = {
    'host': 'localhost',
    'database': 'crimesla',
    'user': 'postgres',
    'password': 'Peach124',
    'port': 5432
}

connection = psycopg2.connect(
    host=db_params['host'],
    database=db_params['database'],
    user=db_params['user'],
    password=db_params['password'],
    port=db_params['port']
)

cursor = connection.cursor()
query = "SELECT * FROM allcrimedata;"
cursor.execute(query)


def read_entry():
    row = cursor.fetchone()
    if row:
        print("Read values:")
        for column_name, value in zip(cursor.description, row):
            print(f"{column_name[0]}: {value}")
    else:
        print("No more entries in the table.")


try:
    while True:
        read_entry()
        time.sleep(5)  # Sleep for 5 seconds before the next iteration

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    # Close the database connection when done
    cursor.close()
    connection.close()

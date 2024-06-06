import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',  # or the address of your MySQL server
}

# Database name to be created
DB_NAME = 'tenant_A_database'
# Path to your .sql file
SQL_FILE_PATH = './tenant_a_database.sql'

# Function to create a database
def create_database(cursor, db_name):
    try:
        cursor.execute(f"CREATE DATABASE {db_name} DEFAULT CHARACTER SET 'utf8'")
        print(f"Database {db_name} created successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database {db_name} already exists.")
        else:
            print(f"Failed creating database: {err}")
            exit(1)

# Function to execute SQL commands from a file
def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as sql_file:
        sql_commands = sql_file.read().split(';')
        for command in sql_commands:
            if command.strip():
                try:
                    cursor.execute(command)
                except mysql.connector.Error as err:
                    print(f"Error executing command: {command}")
                    print(f"MySQL Error: {err}")

# Function to insert a record into the company_master table
def insert_company(cursor, company_data):
    add_company = (
        "INSERT INTO company_master (account_id, company_name, company_email, created_at) "
        "VALUES (%s, %s, %s, %s)"
    )
    cursor.execute(add_company, company_data)

try:
    # Connect to MySQL server
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Create the database
    create_database(cursor, DB_NAME)

    # Select the database
    cursor.execute(f"USE {DB_NAME}")

    # Import the .sql file
    execute_sql_file(cursor, SQL_FILE_PATH)
    print(f"SQL file {SQL_FILE_PATH} imported successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    cnx.close()


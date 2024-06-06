import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',  # or the address of your MySQL server
    'database': 'tenant_A_database',  # specify the database name
}

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

    # Data to be inserted
    company_data = (1, 'The Leela', 'contact@theleela', '2024-05-30 05:52:00')

    # Insert the data
    insert_company(cursor, company_data)

    # Commit the transaction
    cnx.commit()
    print("Company data inserted successfully.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    cursor.close()
    cnx.close()

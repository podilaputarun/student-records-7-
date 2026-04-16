import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DB_password",
        database="university_db"
    )

    return conn

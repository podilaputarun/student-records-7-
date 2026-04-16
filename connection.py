import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Tarun_143",
        database="university_db"
    )

    return conn
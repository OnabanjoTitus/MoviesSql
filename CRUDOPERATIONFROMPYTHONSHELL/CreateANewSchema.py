import mysql.connector

from mysql.connector import Error


def create_dataBase():
    conn = None

    try:
        conn = myDB = mysql.connector.connect(
            host="localhost",
            user="user1",
            password="Welcome@1")
        myCursor = conn.cursor()
        myCursor.execute("CREATE DATABASE myDatabaseFromShell")

        if conn.is_connected():
            print("Database Is created")
    except Error as e:
        print("Cannot be created due to ", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown!!!!')


def main():
    create_dataBase()


if __name__ == '__main__':
    main()

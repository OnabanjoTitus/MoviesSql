# first we import the mysql connector
import mysql.connector

# import the error module from mysql connector
from mysql.connector import Error


# define the connector function
def connect_insert():
    """ function to connect and fetch rows in database"""
    # create a variable for the connector object
    conn = None

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='pentax',
                                       user='user1',
                                       password='Welcome@1',
                                       auth_plugin='mysql_native_password')
        # what to display once connection is successful
        print("Connected to the database")
        if conn.is_connected():
            print("Connected to database")
            db_cursor = conn.cursor()

            # what to display once connection is successful
            sql = "INSERT INTO Human (name, color, sex, Bloodgroup) VALUES (%s,%s,%s,%s)"
            val = [
                # ('Hannah', 'White', 'Female', 'B-'),
                # ('Micheal', 'Brown', 'Male', 'O-'),
                # ('Sandy', 'Black', 'Male', 'O+'),
                # ('Green', 'Yellow', 'Male', 'AB'),
                # ('Richard', 'Black', 'Male', 'B+')



            ]
            db_cursor.executemany(sql, val)

            conn.commit()

            print(db_cursor.rowcount, "row was counted")

            db_cursor.close()

            print("\nPrinting each buyer record")
            # for row in records:
            #     print("Buyer name:", row[0])
            # print("Department:", row[1])
            # print("Position:", row[2])
            # print("Supervisor:", row[3])

    except Error as e:
        print('Not Connecting to the database due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown!!!!')


connect_insert()
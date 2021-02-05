import mysql.connector

from mysql.connector import Error

firstName = input("Enter firstName")
lastName = input("Enter lastName")
middleName = input("Enter middle name")
date = input("Enter date")
number = int(input("enter number"))
occupation = input("occupation")

type = input("Enter the account Type")
status = input("Enter the account status")
openingDate = input("Enter the opening date")

transactionDate = input("Enter the date of transaction")
transactionType = input("enter the transaction type")
amount = int(input("Enter the amount"))
medium = input("Enter the medium of transaction")


def connect_insert_into_bank():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='BANKING_APPLICATION',
                                       user='user1',
                                       password='Welcome@1',
                                       )
        print("Connected to the database")
        if conn.is_connected():
            print("Connected to database")
            db_cursor = conn.cursor()
            customer = "INSERT INTO customers (firstName,lastName," \
                       "middleName,dob,mobileNumber,occupation) VALUES (%s," \
                       "%s,%s,%s,%s,%s) "
            val = [firstName, lastName, middleName, date, number, occupation]
            db_cursor.execute(customer, val)

            customeridquery = f"SELECT customerId from customers where mobileNumber ={number}"
            db_cursor.execute(customeridquery)
            result = db_cursor.fetchone()

            account = "INSERT INTO account(customerId,type,status,openingDate) values (%s,%s,%s,%s)"
            val2 = [result[0], type, status, openingDate]
            db_cursor.execute(account, val2)

            accountidquery = f"SELECT accountNumber from account where customerId"
            db_cursor.execute(accountidquery)

            accountnumber = db_cursor.fetchone()
            print(accountnumber[0])
            transactions = "INSERT INTO transaction(accountNumber,date,type,amount,medium) values (%s,%s,%s,%s,%s)"
            val3 = [accountnumber[0], transactionDate, transactionType, amount, medium]

            db_cursor.execute(transactions, val3)
            conn.commit()

            print(db_cursor.rowcount, "row was counted")

            db_cursor.close()

            print("\nPrinting each buyer record")

    except Error as e:
        print('Not Connecting to the database due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown!!!!')


def main():
    connect_insert_into_bank()


if __name__ == '__main__':
    main()

import mysql.connector
from mysql.connector import Error


def create_tables():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="user1",
            password="Welcome@1",
            database="BANKING_APPLICATION"
        )

        myCursor = conn.cursor()
        customerTable = "CREATE TABLE customers (customerId integer  auto_increment," \
                        " firstName VARCHAR(255), " \
                        "lastName VARCHAR(255), " \
                        "middleName VARCHAR(255),dob DATE, mobileNumber VARCHAR(19) UNIQUE , occupation VARCHAR(255)," \
                        "constraint customer_pk primary key(customerId)) "

        accountTable = "CREATE TABLE account (accountNumber INT   AUTO_INCREMENT,customerId INT not null," \
                       " type VARCHAR(255), status VARCHAR(255), openingDate DATE," \
                       "constraint account_pk primary key(accountNumber),"\
                       "constraint account_fk FOREIGN KEY (customerId) REFERENCES customers(customerId))"

        Transaction = "CREATE TABLE transaction (transactionId INT  AUTO_INCREMENT ," \
                      " accountNumber INT not null, " \
                      "date DATE, type VARCHAR (255)," \
                      "amount INT ,medium VARCHAR(255)," \
                      "constraint transaction_pk primary key (transactionId)," \
                      "constraint  transaction_fk FOREIGN KEY(accountNumber) REFERENCES account(accountNumber))"
        myCursor.execute(customerTable)
        myCursor.execute(accountTable)
        myCursor.execute(Transaction)

        if conn.is_connected():
            print("Table Is created")
    except Error as e:
        print("Cannot be created due to ", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown!!!!')


def main():
    create_tables()


if __name__ == '__main__':
    main()

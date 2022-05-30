'''
@author Philip Holmqvist
'''

import psycopg2

def login_user(email):
    conn = None
    account = None
    try:

        print("Connecting to database...")
        conn = psycopg2.connect(
        host="pgserver.mau.se",
        database="lunchjakt",
        user="am1549",
        password="xibh1ocz")
        print("Connection Success!")
        cursor = conn.cursor()
        statement = f"SELECT * from users WHERE mail='{email}';"
        cursor.execute(statement)
        account = cursor.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return account

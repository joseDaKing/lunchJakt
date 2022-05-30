'''
@author Philip Holmqvist
'''

import psycopg2

from data.find import find
def register_new_user_to_database(email, password, fname, lname):
    conn = None
    try:

        print("Connecting to database...")
        conn = psycopg2.connect(
        host="pgserver.mau.se",
        database="lunchjakt",
        user="am1549",
        password="xibh1ocz")
        print("Connection Success!")

        cursor = conn.cursor()
    

        PostgreSQL_insert = "INSERT INTO users (mail, p_word, f_name, l_name) VALUES (%s, %s, %s, %s)"
        insert_to = (email, password, fname, lname)
        cursor.execute(PostgreSQL_insert, insert_to)
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

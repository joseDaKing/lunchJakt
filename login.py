"""
@author Adrian Rybarczyk & Philip Aronsson
"""

#This file will be rewritten by Adrian Rybarczyk to work with flask
#egna lokala mappar och filer för användare

import psycopg2
from psycopg2 import Error
from flask import Flask
from flask_login import LoginManager, UserMixin
from datetime import datetime

import os


app = Flask(__name__)

SECRET_KEY = os.urandom(32)

app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager()

login_manager.init_app(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'pgserver.mau.se'



def register():

    #Connect to database
    try:
        connection = psycopg2.connect(user = "am1549",
        password = "xibh1ocz",
        host = "pgserver.mau.se",
        port = "5432",
        database = "lunchjakt")
        cursor = connection.cursor()


    #Specific information for function

        customer_password = input("Ange lösenord: ")
        customer_firstname = input("Ange förnamn: ")
        customer_lastname = input("Ange efternamn: ")
        customer_email = input("Ange email: ")

        customer_email = customer_email.lower()

        PostgreSQL_insert = """ INSERT INTO users (mail, p_word, f_name, l_name) VALUES (%s, %s, %s, %s)"""
        insert_to = (customer_email, customer_password, customer_firstname, customer_lastname)
        cursor.execute(PostgreSQL_insert, insert_to)

        connection.commit()
        count = cursor.rowcount
        print(count, f"Registered user {customer_email} successfully!")


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

def login():

    #connect to database
    try:
        connection = psycopg2.connect(user = "am1549",
        password = "xibh1ocz",
        host = "pgserver.mau.se",
        port = "5432",
        database = "lunchjakt")
        cursor = connection.cursor()

        #Specific information for function

        login_email = input("Ange email: ")
        login_password = input("Ange lösenord: ")
        login_email = login_email.lower()

        statement = f"SELECT mail from users WHERE mail='{login_email}' AND p_word = '{login_password}';"
        cursor.execute(statement)

        if not cursor.fetchone():
            print("Login misslyckades! ")
        else:
            print("Välkommen! ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()


register()


"""
@author Adrian Rybarczyk & Philip Aronsson
"""

import psycopg2
from psycopg2 import Error
import re
from flask import Flask, jsonify, redirect, render_template, url_for, request

def register():

    #Connect to database
    try:
        connection = psycopg2.connect(user = "am1549",
        password = "fiqbagvo",
        host = "pgserver.mau.se",
        port = "5432",
        database = "lunchjakt")
        cursor = connection.cursor()


    #Specific information for function

        customer_password = input("Ange lösenord: ")
        customer_firstname = input("Ange förnamn: ")
        customer_lastname = input("Ange efternamn: ")
        customer_email = input("Ange email: ")


        PostgreSQL_insert = """ INSERT INTO användare (email, p_word, f_name, l_name) VALUES (%s, %s, %s, %s)"""
        insert_to = (customer_email, customer_password, customer_firstname, customer_lastname)
        cursor.execute(PostgreSQL_insert, insert_to)

        connection.commit()
        count = cursor.rowcount
        print(count, f"Registered user {customer_username} successfully!")


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

def login():

    #connect to database
    try:
        connection = psycopg2.connect(user = "am1549",
        password = "fiqbagvo",
        host = "pgserver.mau.se",
        port = "5432",
        database = "lunchjakt")
        cursor = connection.cursor()

        #Specific information for function

        login_email = input("Ange email: ")
        login_password = input("Ange lösenord: ")
        statement = f"SELECT mail from users WHERE u_name='{login_email}' AND p_word = '{login_password}';"
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
'''
@author Philip Holmqvist
'''


import re
from flask import Flask, jsonify, redirect, render_template, url_for, request
import psycopg2

from data.find import find;

from forms import SearchForm #För sökning


#from data.Restaurant import Restaurant

app = Flask(__name__)

# För att köra programmet tryck på run knappen.
# Följ sedan länken som dyker upp i terminalen.
#pip install flask-wtf
#pip install wtforms



#Startsidan
@app.route("/")
def home_page():
    return render_template('index.html')

#Vid inloggning blir man omdirigerad till denna sidan. Värden från inloggning finns i variablerna.
@app.route("/", methods=['POST'])
def home_page_login():
    email = request.form['email']
    password = request.form=['password']
    print(email)
    print(password)

    return render_template('index.html')


#Användar sidan där man kan se profil.
@app.route("/user/<input>")
def user_page():
    return render_template('user.html')


#Resturangsidorna, dynamiska. <---------------------
@app.route("/resturant/<name>") 
def resturant_page(name):
    return render_template('resturant.html')

 

#Förslagssidan, dynamisk - beror på input som gjorts. 
@app.route("/suggestions", methods=['GET']) 
def suggestion_page():
    input = request.args.get('searched')
    result = find(search_text = input)
    print(result)
    return render_template('suggestion.html', resturants = result)

'''


def connect():
    conn = None
    try:

        print("Connecting to database...")
        conn = psycopg2.connect(
        host="jdbc:postgresql://pgserver.mau.se",
        database="onlinestore",
        user="****",
        password="****")
        print("Connection Success!")

        cur = conn.cursor()
        cur.execute('INSERT INTO suppliers (namn, phonenumber, adress) VALUES ('"Philip"', '"0706170099"', '"Tyringegatan 3"')')
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

'''

#Main metod för att starta webbservern.     
if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1', port= 8080)

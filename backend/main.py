'''
@author Philip Holmqvist
'''


from flask import Flask, jsonify, render_template
from scraper import *
import psycopg2

app = Flask(__name__)

# För att köra programmet tryck på run knappen.
# Följ sedan länken som dyker upp i terminalen.
#pip install psycopg2


#Startsidan
@app.route("/")
def home_page():
    return render_template('index.html')


#Användar sidan där man kan se profil.
@app.route("/user/<input>")
def user_page():
    return render_template('user.html')


#Resturangsidorna, dynamiska. <---------------------
@app.route("/resturant/<name>") 
def resturant_page(name):
    return getResturantByName(name)
 

#Förslagssidan, dynamisk - beror på input som gjorts. 
@app.route("/suggestions/<input>") 
def suggestion_page(input):
    return render_template('suggestion.html')

'''


def connect():
    conn = None
    try:

        print("Connecting to database...")
        conn = psycopg2.connect(
        host="jdbc:postgresql://pgserver.mau.se",
        database="onlinestore",
        user="am2364",
        password="hej1234")
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

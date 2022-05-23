'''
@author Philip Holmqvist
'''


import re
from flask import Flask, jsonify, redirect, render_template, url_for, request, flash, session, redirect
import psycopg2
import os, sys

from data.find import find

from forms import SearchForm #För sökning

from flask_login import UserMixin, login_user


#from data.Restaurant import Restaurant

app = Flask(__name__)


# För att köra programmet tryck på run knappen.
# Följ sedan länken som dyker upp i terminalen.
#pip install flask-wtf
#pip install wtforms
#pip install pipreqs
#pip install gunicorn

#Hemlig nyckel för användar session.
SECRET_KEY = os.urandom(32)
app.secret_key = SECRET_KEY


#Startsida
#Author Philip Holmqvist 
@app.route("/")
def home_page():
    fname = session.get('fname')
    return render_template('index.html', fname=fname)


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
    fname = session.get('fname')
    return render_template('suggestion.html', resturants = result, fname=fname)

#sida för att regristrera ett nytt konto.
@app.route("/register", methods=['GET','POST'])
def register_page():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'fname' in request.form and 'lname' in request.form:
        email = request.form['email']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']

        account = loginUser(email)

        if account:
            flash('Det finns redan ett konto med denna email adressen!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Ange en giltig email adress!')
        elif not re.match(r'[A-Za-z]+', fname):
            flash('Namn får inte innehålla siffror!')
        elif not re.match(r'[A-Za-z]+', lname):
            flash('Namn får inte innehålla siffror!')     
        elif not email or not password or not fname or not lname:
            flash('Fyll i alla fälten!')
        else:
            #Konto finns inte och datan är godkänd. Vi lägger in kontot i databasen.              
            registerNewUserToDatabase(email, password, fname, lname)
            flash('Konto är registrerat!')
        
        return redirect(url_for('login_page'))

    elif request.method == 'POST': #Ingen data har skickats med i anropet.
        flash('Fyll i fälten!')    

    
    fname = session.get('fname')
    return render_template('register.html', fname=fname)


#sidan för att logga in på sitt konto.
@app.route("/login", methods=['GET', 'POST']) 
def login_page():
    if 'loggedin' in session:
        #Ska inte gå att komma åt egentligen, men utifall att. Omdirigera till startsida.
        flash('Du är redan inloggad')
        return render_template('index.html', fname=session['fname'])

    #Kolla så att email och lösenord har skickats med i POST begäran. (Användare har tryckt logga in)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        #Sparar ner värdena till variabler för enkel åtkomst.
        email = request.form['email']
        password = request.form['password']

        account = loginUser(email=email)

        if account:
            #Kontot existerar
            if password == account[1]:
                flash('Login lyckades!')
                #Skapa sessions data som vi kan komma åt i andra routes.
                session['loggedin'] = True
                session['id'] = account[0]
                session['fname'] = account[2]
                #Redirecta till startsida.
                return redirect(url_for('home_page'))

            else:
                flash('Fel lösenord!')
        else:
            #Kontot finns inte eller så är anv/lösenord fel
            flash('Finns inget konto kopplat till email adressen!')
    
    fname = session.get('fname')
    return render_template('login.html', fname=fname)

@app.route("/logout")
def logout():
    #Ta bort session data, detta kommer logga ut användaren.
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('fname', None)
    #Omdirigera till startsidan
    return redirect(url_for('home_page'))                      

#Profilsidan.
@app.route("/profile", methods=['GET']) 
def profile_page():
    fname = session.get('fname')
    return render_template('profile.html', fname=fname)


def registerNewUserToDatabase(email, password, fname, lname):
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

def loginUser(email):
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


def connect(resturant_id, rating):
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
    

        PostgreSQL_insert = "INSERT INTO ratings (restaurant_id, rating) VALUES (%s, %s)"
        insert_to = (resturant_id, rating)
        cursor.execute(PostgreSQL_insert, insert_to)
        conn.commit()

        

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')



#Main metod för att starta webbservern.     
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port=port, debug=True)

   

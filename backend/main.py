from flask import Flask, jsonify, render_template
from scraper import *

app = Flask(__name__)

# För att köra programmet tryck på run knappen.
# Följ sedan länken som dyker upp i terminalen.


#Startsidan
@app.route("/")
def home_page():
    return render_template('index.html')


#Användar sidan där man kan se profil.
@app.route("/user/<input>")
def user_page():
    return render_template('user.html')


#Resturangsidorna, dynamiska.
@app.route("/resturant/<name>") 
def resturant_page(name):
    scrape(name)
    information = read_Content_From_File() 
    return jsonify(information)
 

#Förslagssidan, dynamisk - beror på input som gjorts. 
@app.route("/suggestions/<input>") 
def suggestion_page(input):
    return render_template('suggestion.html')
  

#Main metod för att starta webbservern.     
if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1', port= 8080)

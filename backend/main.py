from flask import Flask, render_template
from scraper import *

app = Flask(__name__)

# För att köra programmet. Öppna powershell, navigera till mappen och skriv
# $env:FLASK_APP = "main.py"
# $env:FLASK_ENV = "development"cl
# flask run


@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/resturant/<name>")
def resturant_page(name):
    scrape(name)
           
    information = read_Content_From_File() 
    return render_template('index.html', content = information)
  
     
if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1', port= 8080)





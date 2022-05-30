'''
@author Philip Holmqvist
'''

from flask import Flask

from os import urandom, environ

from routes.home import home

from routes.login import login

from routes.logout import logout

from routes.profile import profile

from routes.register import register

from routes.resturant import resturant

from routes.suggestion import suggestion

from routes.user import user

app = Flask(__name__)

app.register_blueprint(home)

app.register_blueprint(login)

app.register_blueprint(logout)

app.register_blueprint(profile)

app.register_blueprint(register)

app.register_blueprint(resturant)

app.register_blueprint(suggestion)

app.register_blueprint(user)

SECRET_KEY = urandom(32)

app.secret_key = SECRET_KEY

if __name__ == '__main__':
    
    port = int(environ.get('PORT', 5000))

    app.run(host = '0.0.0.0', port=port, debug=True)
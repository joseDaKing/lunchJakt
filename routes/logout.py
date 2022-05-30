'''
@author Philip Holmqvist
'''

from flask import Blueprint, redirect, url_for, session

logout = Blueprint(
    name = "logout", 
    import_name = __name__, 
    template_folder="../templates",
    static_url_path = "../static"
)

@logout.route("/logout")
def logout_page():
    #Ta bort session data, detta kommer logga ut användaren.
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('fname', None)
    #Omdirigera till startsidan
    return redirect(url_for('home_page'))                      

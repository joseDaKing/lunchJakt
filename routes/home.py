'''
@author Philip Holmqvist
'''

from flask import Blueprint, render_template, session

home = Blueprint(
    name = "home", 
    import_name = __name__, 
    template_folder="../templates",
    static_url_path = "../static"
)

@home.route("/")
def home_page():
    fname = session.get('fname')
    return render_template('index.html', fname=fname)
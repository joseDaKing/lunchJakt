'''
@author Philip Holmqvist
'''

from flask import Blueprint, render_template

user = Blueprint(
    name = "user", 
    import_name = __name__, 
    template_folder="../templates",
    static_url_path = "../static"
)

@user.route("/user/<input>")
def user_page():
    return render_template('user.html')

'''
@author Philip Holmqvist
'''

from flask import Blueprint, render_template, session

profile = Blueprint(
    name = "profile", 
    import_name = __name__, 
    template_folder="../templates",
    static_url_path = "../static"
)

@profile.route("/profile", methods=['GET']) 
def profile_page():
    fname = session.get('fname')
    return render_template('profile.html', fname=fname)

'''
@author Philip Holmqvist
'''

from flask import Blueprint, render_template

resturant = Blueprint(
    name = "resturant", 
    import_name = __name__, 
    template_folder="../templates",
    static_url_path = "../static"
)

@resturant.route("/resturant/<name>") 
def resturant_page():
    return render_template('resturant.html')

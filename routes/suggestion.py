'''
@author Philip Holmqvist
'''

from flask import Blueprint, render_template, request, session

from data.find import find

suggestion = Blueprint(
    name = "suggestion", 
    import_name = __name__, 
    template_folder="../templates",
    static_url_path = "../static"
)

@suggestion.route("/suggestions", methods=['GET']) 
def suggestion_page():
    input = request.args.get('searched')
    result = find(search_text = input)
    fname = session.get('fname')
    return render_template('suggestion.html', resturants = result, fname=fname)
'''
@author Philip Holmqvist
'''

import re

from flask import Blueprint, redirect, render_template, url_for, request, flash, session

from database.login_user import login_user

from database.register_new_user_to_database import register_new_user_to_database

register = Blueprint(
    name = "register", 
    import_name = __name__, 
    template_folder="../templates",
    static_url_path = "../static"
)

@register.route("/register", methods=['GET','POST'])
def register_page():
    if request.method == "POST":
        hasData = (
            'email' in request.form 
            and 'password' in request.form 
            and 'fname' in request.form 
            and 'lname' in request.form
        )

        if hasData:
            email = request.form['email']
            password = request.form['password']
            fname = request.form['fname']
            lname = request.form['lname']

            account = login_user(email)

            has_account = not not account

            has_valid_email = re.match(r'[^@]+@[^@]+\.[^@]+', email)

            has_valid_firstname = re.match(r'[A-Za-z]+', fname)

            has_valid_lastname = re.match(r'[A-Za-z]+', lname)

            has_fields = email or not password or not fname or not lname

            if has_account:
                flash('Det finns redan ett konto med denna email adressen!')
            elif not has_valid_email:
                flash('Ange en giltig email adress!')
            elif not has_valid_firstname:
                flash('Namn får inte innehålla siffror!')
            elif not has_valid_lastname:
                flash('Namn får inte innehålla siffror!')     
            elif not has_fields:
                flash('Fyll i alla fälten!')
            else:            
                register_new_user_to_database(email, password, fname, lname)

                flash('Konto är registrerat!')
            
            return redirect(url_for('login_page'))
        else:
            flash('Fyll i fälten!')
    
    fname = session.get('fname')

    return render_template('register.html', fname=fname)

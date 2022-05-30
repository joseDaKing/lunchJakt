'''
@author Philip Holmqvist
'''

from flask import Blueprint, redirect, render_template, url_for, request, flash, session

from database.login_user import login_user

login = Blueprint(
    name = "login", 
    import_name = __name__, 
    template_folder="../templates",
    static_url_path = "../static"
)

@login.route("/login", methods=['GET', 'POST']) 
def login_page():
    
    is_logged_in = 'loggedin' in session

    if is_logged_in:
        
        flash('Du är redan inloggad')
        
        return render_template('index.html', fname=session['fname'])

    has_email = 'email' in request.form

    has_password = 'password' in request.form

    is_fields_valid = has_email and has_password
    
    if request.method == 'POST' and is_fields_valid:
        
        email_field = request.form['email']
        
        password_field = request.form['password']

        account = login_user(email=email_field)

        is_account_existing = account != None

        if is_account_existing:

            id = account[0]

            password = account[1]

            first_name = account[2]

            if password == password_field:
                flash('Login lyckades!')
                
                session['loggedin'] = True
                
                session['id'] = id
                
                session['fname'] = first_name
                
                return redirect(url_for('home_page'))

            else:
                flash('Fel lösenord!')
        else:
            flash('Finns inget konto kopplat till email adressen!')
    
    fname = session.get('fname')
    
    return render_template('login.html', fname=fname)

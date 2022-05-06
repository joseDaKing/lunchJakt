#Author Philip Holmqvist
#Formulär som visas upp i html templates.
#Klasserna har fält som måste fyllas i.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SearchForm(FlaskForm):
    searched = StringField(label='Searched')
    submit = SubmitField(label='Submit')

'''
class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address = StringField(label='email)
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')
    submit = SubmitField(label='submit')
'''


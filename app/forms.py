from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=1, max=25, message= "Username length is [1; 25]")])
    password = PasswordField('New Password', [
        validators.Length(min=1, max=25, message= "Password length is [1; 25]")
        #validators.EqualTo('confirm', message='Passwords must match')
    ])
    #confirm = PasswordField('Repeat Password')

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=1, max=25, message= "Username length is [1; 25]")])
    password = PasswordField('New Password', [
        validators.Length(min=1, max=25, message= "Password length is [1; 25]"),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
from app import app, db
from flask import render_template, redirect, flash
from forms import *
from database import User

@app.route('/')
def start_page():
    return render_template("start-page.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
   #print(form.username.data, form.password.data)
    if form.validate_on_submit():
        users = User.query.filter(User.name == form.username.data, User.password == form.password.data).all()
        print(users)
        if (len(users) == 1):
            return render_template('say-hi.html', name=form.username.data)
        else:
            return render_template('login.html', form=form, errors=["Wrong username or password"])
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegistrationForm()
    #print(form.username.data, form.password.data)
    if form.validate_on_submit():
        users = User.query.filter(User.name == form.username.data).all()
        if (len(users) == 0):
            new_user = User(form.username.data, form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return render_template('say-hi.html', name=form.username.data)
        else:
            return render_template('reg.html', form=form, errors=["This username is already taken"])
    return render_template('reg.html', form=form)
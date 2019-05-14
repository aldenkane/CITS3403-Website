from flask import render_template, url_for, flash, redirect, send_from_directory
from app import app
from app.forms import LoginForm

@app.route('/')

@app.route('/index')
def index():
    user = {'username': 'Miguel'} #Pseudo User noise. Might delete with actual user functionality
    return render_template('index.html', title='Home', user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

from flask import render_template, url_for, flash, redirect, send_from_directory, request
from app import app
from app.forms import LoginForm

@app.route('/')

@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/vote')
def vote():
    user = {'username': 'Miguel'}
    return render_template('vote.html', title='Vote', user=user)

@app.route('/results')
def results():
    user = {'username': 'Miguel'}
    return render_template('results.html', title='Results', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

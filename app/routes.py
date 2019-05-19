from flask import render_template, url_for, flash, redirect, send_from_directory, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/vote')
@login_required
def vote():
    poll_data = {'question':'Which car do you want to drive across the Nullarbor?','fields':['Ford Bronco', 'Jeep Wrangler', 'Subaru Outback', 'Tesla Model S', 'Toyota Land Cruiser']}
    return render_template('vote.html', title='Vote', data=poll_data)

@app.route('/poll')
def poll():
    poll_data = {'question':'Which car do you want to drive across the Nullarbor?','fields':['Ford Bronco', 'Jeep Wrangler', 'Subaru Outback', 'Tesla Model S', 'Toyota Land Cruiser']}
    vote = request.args.get('field')
    out = open('data.txt', 'a')
    out.write( vote + '\n' )
    out.close()
    return render_template('thankVote.html', data=poll_data)

@app.route('/results')
def results():
    poll_data = {'question':'Which car do you want to drive across the Nullarbor?','fields':['Ford Bronco', 'Jeep Wrangler', 'Subaru Outback', 'Tesla Model S', 'Toyota Land Cruiser']}
    votes = {}
    for f in poll_data['fields']:
        votes[f] = 0

    f  = open('data.txt', 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1
    return render_template('results.html', data=poll_data, votes=votes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

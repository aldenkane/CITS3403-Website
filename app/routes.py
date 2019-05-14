from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'} #Pseudo User noise. Might delete with actual user functionality
    return render_template('index.html', title='Home', user=user)

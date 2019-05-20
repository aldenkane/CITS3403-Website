import os
basedir = os.path.abspath(os.path.dirname(__file__))

#Miguel Grindberg's "Flask Mega-Tutorial, Chapters 1-8" followed to create config file
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'alden'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
#admin authentication
from admin import AdminView

#Miguel Grindberg's "Flask Mega-Tutorial, Chapters 1-8" followed used to configure app
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
dateFile = 'data.txt'

from app import routes, models
from app.models import User, Topics, Polls, Options


#Administrator Authentications
#Daniel Osaetin's "Flask by Example, Parts 1-7" followed to create administrator dashboard. Topics, Polls, and Options are all not used for this Flask application. Wasn't able to integrate database for polling
admin = Admin(app, name='Dashboard', index_view=AdminView(User, db.session, url='/admin', endpoint='admin'))
admin.add_view(AdminView(Topics, db.session))
admin.add_view(AdminView(Polls, db.session))
admin.add_view(AdminView(Options, db.session))

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
#admin authentication
# from admin import AdminView

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
from app.models import User, Topics, Polls, Options

admin = Admin(app, name='Dashboard')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Topics, db.session))
admin.add_view(ModelView(Polls, db.session))
admin.add_view(ModelView(Options, db.session))

#This has to do with admin authentication
# admin = Admin(app, name='Dashboard', index_view=AdminView(User, db.session, url='/admin', endpoint='admin'))
# admin.add_view(AdminView(Topics, db.session))
# admin.add_view(AdminView(Polls, db.session))
# admin.add_view(AdminView(Options, db.session))

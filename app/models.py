from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#Miguel Grindberg's "Flask Mega-Tutorial, Chapters 1-8" followed to create User class
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#Base model for Polling Options
#Daniel Osaetin's "Flask by Example, Parts 1-7" used to create Base, Topics, Options, and Polls classes. These classes were never used for polling, but could be integrated for future improvements.
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

#Model for poll topics
#Daniel Osaetin's "Flask by Example, Parts 1-7" used to create Base, Topics, Options, and Polls classes. These classes were never used for polling, but could be integrated for future improvements.
class Topics(Base):
    title = db.Column(db.String(500))

    # Display the object
    def __repr__(self):
        return self.title

# Model for poll options
#Daniel Osaetin's "Flask by Example, Parts 1-7" used to create Base, Topics, Options, and Polls classes. These classes were never used for polling, but could be integrated for future improvements.
class Options(Base):
    name = db.Column(db.String(200))

# Polls model for voting
#Daniel Osaetin's "Flask by Example, Parts 1-7" used to create Base, Topics, Options, and Polls classes. These classes were never used for polling, but could be integrated for future improvements.
class Polls(Base):

    # Columns declaration
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    option_id = db.Column(db.Integer, db.ForeignKey('options.id'))
    vote_count = db.Column(db.Integer, default=0)
    status = db.Column(db.Boolean) # to mark poll as open or closed

    # Relationship declaration using ORM
    topic = db.relationship('Topics', foreign_keys=[topic_id], backref=db.backref('options', lazy='dynamic'))
    option = db.relationship('Options',foreign_keys=[option_id])

    def __repr__(self):
        return self.option.name

from app import app, db

from app.models import User, Base, Topics, Options, Polls

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Base': Base, 'Topics': Topics, 'Options': Options, 'Polls':Polls}

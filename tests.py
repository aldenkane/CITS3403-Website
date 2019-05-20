from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User

#Miguel Grindberg's "Flask Mega-Tutorial, Chapters 1-8" followed to create unit tests, including setUp, tearDown, test_password_hashing
class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
#Miguel Grindberg's "Flask Mega-Tutorial, Chapters 1-8" followed to create unit tests, including setUp, tearDown, test_password_hashing
    def test_password_hashing(self):
        u = User(username='foo')
        u.set_password('foo')
        self.assertFalse(u.check_password('bar'))
        self.assertTrue(u.check_password('foo'))

if __name__ == '__main__':
    unittest.main(verbosity=2)

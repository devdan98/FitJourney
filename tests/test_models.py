import unittest
from app import create_app, db
from app.models import User

class UserModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('app.config.TestingConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        user = User(age=25, weight=70.0, height=175.0, gender='male', goal='gain muscle', equipment='dumbbells,barbell')
        db.session.add(user)
        db.session.commit()
        self.assertIsNotNone(user.id)

if __name__ == '__main__':
    unittest.main()

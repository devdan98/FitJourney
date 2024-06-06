import unittest
from app import create_app, db
from app.models import User
import json

class UserRoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('app.config.TestingConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        response = self.client.post('/user', json={
            'age': 25,
            'weight': 70.0,
            'height': 175.0,
            'gender': 'male',
            'goal': 'gain muscle',
            'equipment': ['dumbbells', 'barbell']
        })
        self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        user = User(age=25, weight=70.0, height=175.0, gender='male', goal='gain muscle', equipment='dumbbells,barbell')
        db.session.add(user)
        db.session.commit()
        response = self.client.get(f'/user/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['age'], 25)

if __name__ == '__main__':
    unittest.main()

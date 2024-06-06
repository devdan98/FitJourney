import unittest
from app.services import generate_workout, generate_meal_plan
from app.models import User

class ServicesTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User(age=25, weight=70.0, height=175.0, gender='male', goal='gain muscle', equipment='dumbbells,barbell')

    def test_generate_workout(self):
        workout_plan = generate_workout(self.user)
        self.assertIn('workout', workout_plan.lower())

    def test_generate_meal_plan(self):
        meal_plan = generate_meal_plan(self.user)
        self.assertIn('meal', meal_plan.lower())

if __name__ == '__main__':
    unittest.main()

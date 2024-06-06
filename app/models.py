from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    goal = db.Column(db.String(50), nullable=False)
    equipment = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'age': self.age,
            'weight': self.weight,
            'height': self.height,
            'gender': self.gender,
            'goal': self.goal,
            'equipment': self.equipment.split(',')
        }

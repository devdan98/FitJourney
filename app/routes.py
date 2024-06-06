from flask import Blueprint, request, jsonify
from .models import User
from . import db
from .services import generate_workout, generate_meal_plan

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to FitJourney API"

@main.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        age=data['age'],
        weight=data['weight'],
        height=data['height'],
        gender=data['gender'],
        goal=data['goal'],
        equipment=",".join(data['equipment'])
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@main.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@main.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.query.get_or_404(user_id)
    user.age = data.get('age', user.age)
    user.weight = data.get('weight', user.weight)
    user.height = data.get('height', user.height)
    user.gender = data.get('gender', user.gender)
    user.goal = data.get('goal', user.goal)
    user.equipment = ",".join(data.get('equipment', user.equipment.split(',')))
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@main.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

@main.route('/workout/<int:user_id>', methods=['GET'])
def get_workout(user_id):
    user = User.query.get_or_404(user_id)
    workout_plan = generate_workout(user)
    return jsonify({'workout_plan': workout_plan})

@main.route('/mealplan/<int:user_id>', methods=['GET'])
def get_meal_plan(user_id):
    user = User.query.get_or_404(user_id)
    meal_plan = generate_meal_plan(user)
    return jsonify({'meal_plan': meal_plan})

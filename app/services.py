import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_workout(user):
    prompt = f"""
    Create a workout plan for a {user.age} year old {user.gender} who weighs {user.weight} kg, is {user.height} cm tall, and has access to the following equipment: {user.equipment}. The goal is {user.goal}.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text

def generate_meal_plan(user):
    prompt = f"""
    Create a meal plan for a {user.age} year old {user.gender} who weighs {user.weight} kg, is {user.height} cm tall, and wants to {user.goal}. Include daily caloric intake and macronutrient breakdown.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text

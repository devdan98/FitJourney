# FitJourney

FitJourney is a Flask-based application for personalized workout and nutrition plans.

## Setup

1. Create a virtual environment:

    ```bash
    python -m venv env
    ```

2. Activate the virtual environment:

    ```bash
    # On Windows
    .\env\Scripts\activate

    # On macOS/Linux
    source env/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    flask run
    ```

## Configuration

Update the `app/config.py` file with your OpenAI API key and other configurations.

## Endpoints

- `POST /user`: Create a new user.
- `GET /user/<int:user_id>`: Retrieve a user.
- `PUT /user/<int:user_id>`: Update a user.
- `DELETE /user/<int:user_id>`: Delete a user.
- `GET /workout/<int:user_id>`: Get workout plan for a user.
- `GET /mealplan/<int:user_id>`: Get meal plan for a user.

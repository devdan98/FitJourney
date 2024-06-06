from app import create_app, db
from flask_migrate import Migrate

app = create_app('app.config.DevelopmentConfig')  # Adjust config as needed
migrate = Migrate(app, db)

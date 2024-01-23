from flask import Flask
from routes import routes
from routes.db import *
from datetime import datetime, timedelta
# from decouple import Config, Csv

app = Flask(__name__)

# Use decouple to read configuration from a .env file or environment variables
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['PERMANENT_SESSION_LIFETIME'] = Config.PERMANENT_SESSION_LIFETIME
db.init_app(app)

app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create main.db tables
    app.run(debug=True, host="0.0.0.0", port=5000)

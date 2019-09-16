from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

def create_app(config_name):
    app.config.from_object(config_options[config_name])
    from .main import main as main_b
    app.register_blueprint(main_b)
    from .auth import auth as auth_b
    app.register_blueprint(auth_b)


    return app
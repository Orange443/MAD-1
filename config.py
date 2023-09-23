# config.py
from dotenv import load_dotenv
from os import getenv

load_dotenv()
def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

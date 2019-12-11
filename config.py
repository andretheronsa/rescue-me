from os import environ, path

# Prepare environment from dotenv file
basedir = path.abspath(path.dirname(__file__))

class Config:
    """Set Flask configuration vars from .env file."""

    # General config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application")

    # Database config -DATABASE_URL is used by Heroku by default
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') \
        or 'sqlite:///' + path.join(basedir, 'app.db')

    # API keys
    GOOGLE_API = environ.get("GOOGLE_API")
    if not GOOGLE_API:
        raise ValueError("No GOOGLE_API set for Flask application")
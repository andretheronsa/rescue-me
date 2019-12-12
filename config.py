from os import environ, path

# Prepare environment from dotenv file
basedir = path.abspath(path.dirname(__file__))

class Config:
    """Set Flask configuration vars from .env file."""

    # General config
    SECRET_KEY = environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application")
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')

    # Database config -DATABASE_URL is used by Heroku by default
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') \
        or 'sqlite:///' + path.join(basedir, 'app.db')

    # API keys
    GOOGLE_API = environ.get("GOOGLE_API")
    if not GOOGLE_API:
        raise ValueError("No GOOGLE_API set for Flask application")
    W3W_API=environ.get("W3W_API")
    if not W3W_API:
        raise ValueError("No W3W_API set for Flask application")
    MAPBOX_API=environ.get("MAPBOX_API")
    if not MAPBOX_API:
        raise ValueError("No MAPBOX_API set for Flask application")
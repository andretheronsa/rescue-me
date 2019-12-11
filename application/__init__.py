from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from flask_login import LoginManager
from flask_session import Session
from flask_migrate import Migrate
from config import Config
import logging
import os

db = SQLAlchemy()

# App factory
def create_app():
    '''Initialize the core application - loading instance relative configs if available'''
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    # Prepare login tools and direct login required to login route
    login = LoginManager(app)
    login.login_view = 'login'
    
    # Init Plugins
    heroku = Heroku(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Creating the critical app context
    with app.app_context():
        from . import routes, models, forms, auth

    # Ensure logging to stout for heroku
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

    return app

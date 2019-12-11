from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from flask_login import LoginManager
from flask_session import Session
from flask_migrate import Migrate
from config import Config
import logging
import os

# Init global plug ins
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login'
heroku = Heroku()
bootstrap = Bootstrap()

# App factory
def create_app(config_class=Config):
    '''Initialize the core application - loading instance relative configs if available'''
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Prepare app instance
    login.init_app(app)
    db.init_app(app)
    heroku.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    
    # Creating the critical app context
    with app.app_context():
        from . import routes, models, forms

    # Ensure logging to stout for heroku
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

    return app

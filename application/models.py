from application import db, login
from flask_login import LoginManager
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import pytz

# Define user loader
@login.user_loader
def load_user(id):
    '''Load given user ID'''
    return User.query.get(int(id))
   
class User(UserMixin, db.Model):
    """Model for user data"""
    
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128), unique=False)
    
    # Relationships
    tracks = db.relationship('Track', backref='username', lazy='dynamic')
    
  
    # Functions #
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Track(db.Model):
    """Model for tracks"""
    
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)
    alias = db.Column(db.String(30), index=True)
    url = db.Column(db.String(70), unique=True)
    create_time = db.Column(db.DateTime, index=True, default=dt.utcnow)
    share_team = db.Column(db.Boolean())
    user_name = db.Column(db.String(64))
    
    # Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    locations = db.relationship('Location', backref='location_id', lazy='dynamic')
    
class Location(db.Model):
    """Model for Location data"""
    
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15))
    logtime = db.Column(db.DateTime, index=True, default=dt.now)
    latitude = db.Column(db.Numeric(8,6))
    longitude = db.Column(db.Numeric(9,6))
    positionAccuracy = db.Column(db.Float())
    altitude = db.Column(db.Float())
    altitudeAccuracy = db.Column(db.Float())
    speed = db.Column(db.Float())
    heading = db.Column(db.Float())
    w3w = db.Column(db.String(60))
    timeStamp = db.Column(db.DateTime(), index=True)
    
    # Relationships
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'))


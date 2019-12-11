from . import db
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
   
# Create user schema
class User(UserMixin, db.Model):
    """Model for user data"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128), unique=False)
    authenticated = db.Column(db.Boolean, unique=False, default=False)
    tracks = db.relationship('Track', backref='username', lazy='dynamic')
  
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Default print for object
    def __repr__(self):
        return '<User {}>'.format(self.username)

'''# Load user
@login.user_loader
def load_user(id):
    return User.query.get(int(id))'''

# Create db classes
class Track(db.Model):
    """Model for tracking data"""
    __tablename__ = "Tracks"
    id = db.Column(db.Integer, primary_key=True)
    tracking_id = db.Column(db.String(20), index=True, unique=True)
    ip = db.Column(db.String(15))
    latitude = db.Column(db.Numeric(8,6))
    longitude = db.Column(db.Numeric(9,6))
    positionAccuracy = db.Column(db.Float())
    altitude = db.Column(db.Float())
    altitudeAccuracy = db.Column(db.Float())
    speed = db.Column(db.Float())
    heading = db.Column(db.Float())
    logtime = timestamp = db.Column(db.DateTime, index=True, default=dt.utcnow)
    timeStamp = db.Column(db.DateTime(), index=True)
    auth_user = db.Column(db.Integer, db.ForeignKey('users.id'))

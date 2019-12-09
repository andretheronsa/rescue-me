
from app import db

# Create db classes
class Tracking(db.Model):
    __tablename__ = "Tracking"
    id = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Geography(50))
    positionAccuracy = db.Column(db.Float4(50))
    altitude = db.Column(db.Float4(50))
    altitudeAccuracy = db.Column(db.Float4(50))
    speed = db.Column(db.Float4(50))
    heading = db.Column(db.Float4(50))
    timeStamp = db.Column(db.String(50))

# Create db class
class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__ (self, mydata):
        self.mydata = mydata
from app import db

class Patient(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String())
    latitude = db.Column(db.String())
    longitude = db.Column(db.String())

    def __init__(self, ip, latitude, longitude):
        self.ip = ip
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'ip': self.ip,
            'latitude': self.latitude,
            'longitude':self.longitude
        }
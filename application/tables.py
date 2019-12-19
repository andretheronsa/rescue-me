
from flask_table import Table, Col
from application.models import User

class LocationTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']
    id = Col('Id', show=False)
    latitude = Col('Latitude')
    longitude = Col('Longitude')
    positionAccuracy = Col('Position Accuracy (m)')
    altitude = Col('Altitude (m above WGS84)')
    altitudeAccuracy = Col('Altitude Accuracy (m)')
    speed = Col('Speed (m/s)')
    heading = Col('Heading (deg)')
    w3w = Col('What3words')
    ip = Col('IP')
    timeStamp = Col('GPS logtime')
    logtime = Col('Database logtime')
    
class TrackTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']
    id = Col('Id', show=False)
    alias = Col('Name')
    url = Col('Share link')
    create_time = Col('Link create time')
    user_id = Col('Owner')
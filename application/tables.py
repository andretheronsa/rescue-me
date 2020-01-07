
from flask_table import Table, Col, ButtonCol
from application.models import User
from flask import url_for

class TrackTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']
    id = Col('Id', show=False)
    
    create_time = Col('Create time')
    alias = Col('Name')
    url = Col('Share link')
    user_name = Col('Owner') 
    
    showTrackButton = ButtonCol('Show track', 'dashboard', url_kwargs=dict(track_id='id'))

class LocationTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']

    id = Col('Id', show=False)
    timeStamp = Col('Timestamp (device local time)')
    latitude = Col('Latitude (Decimal Degree WGS84)')
    longitude = Col('Longitude (Decimal Degree WGS84)')
    positionAccuracy = Col('Position Accuracy (M)')
    altitude = Col('Altitude (M above WGS84)')
    altitudeAccuracy = Col('Altitude Accuracy (M)')
    speed = Col('Speed (M/S)')
    heading = Col('Heading (Deg)')
    w3w = Col('What3words')
    ip = Col('IP')
    
    showTrackButton = ButtonCol('Show point', 'dashboard', url_kwargs=dict(location_id='id'))
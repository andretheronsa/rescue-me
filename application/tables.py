
from flask_table import Table, Col, ButtonCol
from application.models import User
from flask import url_for

class TrackTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']
    allow_sort = True
    id = Col('Id', show=False)
    alias = Col('Name')
    url = Col('Share link')
    create_time = Col('Link create time')
    user_id = Col('Owner')
    
    name = ButtonCol('Show track', 'dashboard', url_kwargs=dict(track_id='id'))
    
    def sort_url(self, col_key, reverse=False):
        if reverse:
            direction =  'desc'
        else:
            direction = 'asc'
        return url_for('dashboard', sort=col_key, direction=direction)

class LocationTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']
    allow_sort = True

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
        
    def sort_url(self, col_key, reverse=False):
        if reverse:
            direction =  'desc'
        else:
            direction = 'asc'
        return url_for('dashboard', sort=col_key, direction=direction)

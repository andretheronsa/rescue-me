
from flask_table import Table, Col, ButtonCol
from application.models import User
from flask import url_for

class TrackTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']
    allow_sort = True
    id = Col('Id', show=False)
    
    create_time = Col('Create time')
    alias = Col('Name')
    url = Col('Share link')
    user_name = Col('Owner') 
    
    showTrackButton = ButtonCol('Show track', 'dashboard', url_kwargs=dict(track_id='id'))
    
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
    timeStamp = Col('GPS logtime')
    latitude = Col('Latitude (DD)')
    longitude = Col('Longitude (DD)')
    positionAccuracy = Col('Position Accuracy (M)')
    altitude = Col('Altitude (M above WGS84)')
    altitudeAccuracy = Col('Altitude Accuracy (M)')
    speed = Col('Speed (M/S)')
    heading = Col('Heading (Deg)')
    w3w = Col('What3words')
    ip = Col('IP')
    
    showTrackButton = ButtonCol('Show point', 'dashboard', url_kwargs=dict(location_id='id'))
    
    def sort_url(self, col_key, reverse=False):
        if reverse:
            direction =  'desc'
        else:
            direction = 'asc'
        return url_for('dashboard', sort=col_key, direction=direction)

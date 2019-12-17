
from flask_table import Table, Col

class LocationTable(Table):
    id = Col('Id', show=False)
    ip = Col('ip')
    logtime = Col('logtime')
    latitude = Col('latitude')
    longitude = Col('longitude')
    positionAccuracy = Col('positionAccuracy')
    altitude = Col('altitude')
    altitudeAccuracy = Col('altitudeAccuracy')
    speed = Col('speed')
    heading = Col('heading')
    w3w = Col('w3w')
    timeStamp = Col('timeStamp')
    
class TrackTable(Table):
    id = Col('Id', show=False)
    name = Col('name')
    alias = Col('alias')
    url = Col('url')
    create_time = Col('create_time')
    share_team = Col('share_team')
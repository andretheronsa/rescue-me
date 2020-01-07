var map = L.map('mapid').setView([latitude, longitude], 14);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 22,
    id: 'mapbox/outdoors-v11',
    accessToken: MAPBOX_API
}).addTo(map);
if(point == 'true'){
    if(positionAccuracy != 'None'){
        var rad_num = Number(positionAccuracy)
        if(rad_num>0){
            var circle = L.circle([latitude, longitude], {
                color: 'red',
                fillColor: '#f03',
                fillOpacity: 0.2,
                radius: rad_num
            }).addTo(map);
        }
    }
    var marker = L.marker([latitude, longitude]).addTo(map);
    marker.bindPopup("Time: "+timeStamp+
        "<br>Latitude (dec deg): "+latitude+
        "<br>longitude (dec deg): "+longitude+
        "<br>altitude (WGS84): "+altitude+
        "<br>Position Accuracy (m): "+positionAccuracy+
        "<br>Altitude Accuracy (m): "+altitudeAccuracy+
        "<br>Speed (m/s): "+speed+
        "<br>Heading (deg): "+heading+
        "<br>What3Words: "+ W3W
        ).openPopup()
   };
if(line == 'true'){
    var polyline = L.polyline(line_data, {color: 'blue'}).addTo(map);
    map.fitBounds(polyline.getBounds());
};
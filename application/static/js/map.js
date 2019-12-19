var mymap = L.map('mapid').setView([latitude, longitude], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/satellite-v9',
    accessToken: MAPBOX_API
}).addTo(mymap);
if(positionAccuracy != 'None'){
    var rad_num = Number(positionAccuracy)
    if(rad_num>0){
        var circle = L.circle([latitude, longitude], {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: rad_num
        }).addTo(mymap);
    }
}
var marker = L.marker([latitude, longitude]).addTo(mymap);
marker.bindPopup("Latitude (dec deg): "+latitude+
    "<br>longitude (dec deg): "+longitude+
    "<br>altitude (WGS84): "+altitude+
    "<br>Position Accuracy (m): "+positionAccuracy+
    "<br>Altitude Accuracy (m): "+altitudeAccuracy+
    "<br>Speed (m/s): "+speed+
    "<br>Heading (deg): "+heading+
    "<br>What3Words: "+ W3W
    ).openPopup();
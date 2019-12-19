var LATLON = L.marker(L.latLng(LAT,LON));
var mymap = L.map('map').setView([LATLON], 13);
var marker = L.marker([LATLON]).addTo(mymap);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: MAPBOX_API
}).addTo(mymap);
var circle = L.circle([LATLON], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: RAD
}).addTo(mymap);
marker.bindPopup("<b>Lat, long: "+LATLON+"</b><br>What3Words: "+ W3W)+"</b><br>Accuracy (m): "+ RAD+"</b>".openPopup();
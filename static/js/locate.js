var id = 0
var output = document.getElementById('output')
var map = document.getElementById("map")
function locate(){
  function monitorLocation(position) {
    if(geoPosition.init()) {
      var options = {
        timeout:60000, 
        enableHighAccuracy: true,
        maximumAge: 60000};
        geoPosition.getCurrentPosition(updateLocation, errorHandler, options);
    } else {
      output.innerHTML = "Sorry, browser does not support geolocation!";
    }
  }
  function updateLocation(position) {
      sendLocation(position);
      displayLocation(position);
      mapLocation(position)
  }
  function errorHandler(err) {
    if(err.code == 1) {
      output.innerHTML = "Error: Access is denied! Please accept location tracking for this site"
    } else if( err.code == 2) {
      output.innerHTML = "Error: Position is unavailable! Attempting with low accuracy mode...";
    }
  }
  function displayLocation(position) {
      output.innerHTML = 
      "Latitude (decimal degrees): " + Number(position.coords.latitude).toFixed(5) + 
      "<br>Longitude (decimal degrees): " + Number(position.coords.longitude).toFixed(5) +
      "<br>Position accuracy (meters): " + Number(position.coords.accuracy).toFixed(0) +
      "<br>Altitude (meters): " + Number(position.coords.altitude).toFixed(0) +
      "<br>Altitude accuracy (meters): " + Number(position.coords.altitudeAccuracy).toFixed(0) +
      "<br>Time retrieved: " + Date(position.timestamp).toLocaleString();
  }
  function sendLocation(position) {
       $.ajax({
          method: "POST",
          url: '/',
          contentType: "application/json",
          data: JSON.stringify({
            "latitude": position.coords.latitude,
            "longitude": position.coords.longitude,
            "positionAccuracy": position.coords.accuracy,
            "altitude": position.coords.altitude,
            "altitudeAccuracy": position.coords.altitudeAccuracy,
            "speed": position.coords.speed,
            "heading": position.coords.heading,
            "timeStamp": position.timestamp
          }),
          datatype: "json"
        });
  }
  function mapLocation(position) {
    var latlon = position.coords.latitude + "," + position.coords.longitude;
    var GOOGLE_API = '{{ GOOGLE_API }}'
    var img_url = "https://maps.googleapis.com/maps/api/staticmap?"+
      "center="+latlon+"&"+
      "zoom=17"+
      "&scale=2&"+
      "size=600x300&"+
      "maptype=hybrid&"+
      "key="+GOOGLE_API
      "format=png&"+
      "visual_refresh=true&"+
      "markers=size:small%7Ccolor:0xff0000%7Clabel:X%7C"+latlon;
    map.innerHTML = "<img src='"+img_url+"'>";
  }
  monitorLocation()
  id = setInterval(monitorLocation, 60000);
}
function stopMonitoring(id){
  clearInterval(id)
}
function change() {
  var elem = document.getElementById("monitor_button");
  if (elem.value=="false") {
    elem.value = "true";
    elem.innerHTML='STOP TRACKING';
    locate();
  }  else {
    elem.value = "false";
    elem.innerHTML='START TRACKING';
    stopMonitoring(id);
  }
}
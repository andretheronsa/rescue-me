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
      output.innerHTML = "Error: Location access was not approved for tracking - please give sete permissions in options or try again in incognito mode"
    } else if( err.code == 2) {
      output.innerHTML = "Error: Position is unavailable!";
    }
  }
  function displayLocation(position) {
      output.innerHTML = 
      "What3words: " + String(w3w) +
      "<br>Latitude (decimal degrees): " + Number(position.coords.latitude).toFixed(5) + 
      "<br>Longitude (decimal degrees): " + Number(position.coords.longitude).toFixed(5) +
      "<br>Altitude (meters): " + Number(position.coords.altitude).toFixed(0) +
      "<br>Accuracy (meters): " + Number(position.coords.accuracy).toFixed(0) +
      "<br>Time located: " + Date(position.timestamp).toLocaleString();
  }
  function sendLocation(position) {
       $.ajax({
          method: "POST",
          contentType: "application/json",
          data: JSON.stringify({
            "latitude": position.coords.latitude,
            "longitude": position.coords.longitude,
            "positionAccuracy": position.coords.accuracy,
            "altitude": position.coords.altitude,
            "altitudeAccuracy": position.coords.altitudeAccuracy,
            "speed": position.coords.speed,
            "heading": position.coords.heading,
            "timeStamp": Date(position.timestamp).toLocaleString()
          }),
          datatype: "json"
        });
  }
  function mapLocation(position) {
    var latlon = position.coords.latitude + "," + position.coords.longitude;
    var img_url = "https://maps.googleapis.com/maps/api/staticmap?"+
      "center="+latlon+"&"+
      "zoom=17"+
      "&scale=2&"+
      "size=600x300&"+
      "maptype=hybrid&"+
      "key="+GOOGLE_API+"&"+
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
    elem.style.backgroundColor = "LightCoral";
    elem.innerHTML='STOP TRACKING';
    locate();
  }  else {
    elem.value = "false";
    elem.style.backgroundColor = "GreenYellow";
    elem.innerHTML='START TRACKING';
    stopMonitoring(id);
  }
}
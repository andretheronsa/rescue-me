var id = 0
var output = document.getElementById('output')
output.innerHTML = "Toggle tracking button and allow tracking in your browser. <br> Location data will be uploaded every 30s as long as browser window is open"
var map = document.getElementById("map")
var w3w = document.getElementById("w3w")
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
      w3wLocation(position);
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
      "Latitude (decimal degrees): " + Number(position.coords.latitude).toFixed(5) + 
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
      "&scale=1&"+
      "size=600x300&"+
      "maptype=hybrid&"+
      "key="+GOOGLE_API+"&"+
      "format=png&"+
      "visual_refresh=true&"+
      "markers=size:small%7Ccolor:0xff0000%7Clabel:X%7C"+latlon;
    map.innerHTML = "<img src='"+img_url+"'>";
  }
  function w3wLocation(position){
    what3words.api.convertTo3wa({lat:position.coords.latitude, lng:position.coords.longitude})
    .then(function(response) {
      w3w.innerHTML = "What3Words: "+response.words;
   })
   .catch(function(error) { // catch errors here
    console.log("[code]", error.code);
    console.log("[message]", error.message);
  });
  }
  monitorLocation()
  id = setInterval(monitorLocation, 30000);
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
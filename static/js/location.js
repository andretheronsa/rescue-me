var output = document.getElementById('output')
function showLocation(position) {
    console.log("Updated position")
    output.innerHTML = 
      "Latitude (decimal degrees): " + position.coords.latitude + 
      "<br>Longitude (decimal degrees): " + position.coords.longitude +
      "<br>Position accuracy (meters): " + position.coords.accuracy +
      "<br>Altitude (meters): " + position.coords.altitude + 
      "<br>Altitude accuracy (meters): " + position.coords.altitudeAccuracy +
      "<br>Speed (meters per second): " + position.coords.speed + 
      "<br>Heading (Degrees clockwise from North = 0): " + position.coords.heading;
    sendPost(position);
}
function errorHandler(err) {
    if(err.code == 1) {
      output.innerHTML = "Error: Access is denied!";
    } else if( err.code == 2) {
      output.innerHTML = "Error: Position is unavailable!";
    }
}
function getLocation() {
    if(navigator.geolocation) {
      var options = {timeout:60000};
      navigator.geolocation.getCurrentPosition(showLocation, errorHandler, options);
    } else {
      output.innerHTML = "Sorry, browser does not support geolocation!";
    }
}
function monitorLocation(position) {
  if(navigator.geolocation) {
    var options = {timeout:60000};
    navigator.geolocation.watchPosition(showLocation, errorHandler, options);
  } else {
    output.innerHTML = "Sorry, browser does not support geolocation!";
  }
}
function sendPost(position) {
    $.ajax({
        type: "POST",
        url: '/',
        data: {"latitude": position.coords.latitude, "longitude": position.coords.longitude},
    });
}
window.onload = getLocation();
window.onload = monitorLocation();

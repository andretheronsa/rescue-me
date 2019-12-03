var output = document.getElementById('output')
function showLocation(position) {
    var latitude = position.coords.latitude
    var longitude = position.coords.longitude
    output.innerHTML = "Latitude : " + latitude + "<br>Longitude: " + longitude;
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
function sendPost() {
    $.ajax({
        type: "POST",
        url: '/',
        data: {"latitude": latitude, "longitude": longitude},
        success: success
    });
}
window.onload = getLocation;
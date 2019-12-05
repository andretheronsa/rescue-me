var output = document.getElementById('output')
function showLocation(position) {
    output.innerHTML = "Latitude (client): " + position.coords.latitude + "<br>Longitude (client): " + position.coords.longitude;
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
function sendPost(position) {
    $.ajax({
        type: "POST",
        url: '/',
        data: {"latitude": position.coords.latitude, "longitude": position.coords.longitude},
    });
}
window.onload = getLocation();

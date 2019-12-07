// Entire script is a function so it can be called by button
function monitoring(){
  // Specify output HTML elemt to print location data
  var output = document.getElementById('output')
  var status = document.getElementById('output')
  function monitorLocation(position) {
    if(navigator.geolocation) {
      var options = {timeout:60000};
      id = navigator.geolocation.watchPosition(updateLocation, errorHandler, options);
      return id
    } else {
      output.innerHTML = "Sorry, browser does not support geolocation!";
    }
  }
  // Send location to server, display and show a map
  function updateLocation(position) {
      sendLocation(position);
      displayLocation(position);
      mapLocation(position)
  }
  // Handle errors
  function errorHandler(err) {
    if(err.code == 1) {
      output.innerHTML = "Error: Access is denied! Please accept location tracking for this site";
    } else if( err.code == 2) {
      output.innerHTML = "Error: Position is unavailable!";
    }
  }
  // Display location
  function displayLocation(position) {
      output.innerHTML = 
      "Latitude (decimal degrees): " + Number(position.coords.latitude).toFixed(5) + 
      "<br>Longitude (decimal degrees): " + Number(position.coords.longitude).toFixed(5) +
      "<br>Position accuracy (meters): " + Number(position.coords.accuracy).toFixed(0) +
      "<br>Altitude (meters): " + Number(position.coords.altitude).toFixed(0) +
      "<br>Altitude accuracy (meters): " + Number(position.coords.altitudeAccuracy).toFixed(0) +
      "<br>Speed (meters per second): " + Number(position.coords.speed).toFixed(0) +
      "<br>Heading (Degrees clockwise where north = 0): " + Number(position.coords.heading).toFixed(0) +
      "<br>Time retrieved: " + Date(position.timestamp).toLocaleString();
  }
  // Send location to server
  function sendLocation(position) {
       $.ajax({
          method: "POST",
          url: '/tracking',
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
  // Map location
  function mapLocation(position) {
    var lonlat = position.coords.longitude + "," + position.coords.latitude;
    var img_url = "https://static-maps.yandex.ru/1.x/?lang=en-US&ll="+lonlat+"&z=17&l=sat&size=600,300&pt="+lonlat+",flag";
    document.getElementById("mapholder").innerHTML = "<img src='"+img_url+"'>";
  }
  // Run script
  id = monitorLocation();
}
function stopMonitoring(id){
  navigator.geolocation.clearWatch(id);
  document.getElementById("mapholder").innerHTML = ""
}


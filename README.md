RescueMe

**Problem statement and gap analysis**
* People don't plan on being rescued
* Most phones are capable of accurate geolocation
* Many people don't know how to share their location
* People generally don't have location apps on their phone and getting GPS coordinates is not that trivial
* Location aware apps that can share location often do it in a specific format (wastsapp pin) that can't be entered into Heli/GPS etc.
* Reception in the mountains is poor - so downloading an app like what3words is not ideal
* Patients are typically in distress and unable to follow detailed phone instructions
* Patients are typically not experts in relying information and may mess up coordinate systems, lat/longs, decimal places etc.
* Nearly all phones models have a browser with geolocation abilities that can be used using standardised Javascript
* If we controll the server running a website with tracking then the patient does not need to be in the loop
* Cloud based platforms such as AWS and Heroku can run and scale web services as required for very little cost (free tiers are enough for local teams) and not be affected by loadshedding
* Python web frameworks such as Flask make it simple to build run a web application

**Aim**
* To build a tool that takes the patient out of the geolocation loop while making it simple for the rescue team to track the patient.

**Objective**
* Rescue team side
    1. Simple tool to generate a short, sharable, memorable, unique tracking link
    2. Dashboard where rescuers can view all tracks in table and map format.

* Patient side
    1. Must recieve a short, memorable url to follow
    2. Website determines accurate geolocation of the patient using JS
    3. Runs with minimal user input
    4. Runs with minimal internet connectivity
    5. Is very lightweight
    6. Works on most internet connected devices - older phone models should be supported
    7. Sends tracking data to server and notifies patient of successful upload
    8. Show basic location information to patient

**How it works**
* RescueMe is a browser based tracking tool that runs in the cloud (app only wakes up when accessed)
* Rescuer gets unique url from server 
* Send the URL to patient (via sms/watsapp/voice) and instruct patient to:
    1. Ensure location services is active on device
    2. Follow link 
    3. Click the "start tracking" button
    4. Allow tracking when broser asks for permission (This MUST be accepted)
* Rescuers now have access to a map and table of patient data on the server including:
    - Latitude (decimal degrees rounded to 5 places (~1m) relative to WGS84)
    - Longitude (decimal degrees rounded to 5 places (~1m) relative to WGS84)
    - Position accuracy (meters)
    - Altitude (meters above the WGS84 ellipsoid (~30m out in the cape))
    - Altidude accuracy (meters)
    - Speed (meters per second)
    - Heading (degrees)
    - User phone address (mac ID and IP)
    - Time since last call
* Geolocation updated as long as patient has site open
* Geolocation is based on device GPS coordinates if possible (accuracy in 10m range)
* If GPS is not available it falls back on tower triangulation (1000m range)
* If triangulation is not possible it falls back on IP address (very low accuracy)
* Any authorized rescuer can view patient location and history if tracking link was made sharable
* App sends back basic info to patient
    - Location in decimal degrees
    - what2words location
    - Low resolution aeiral imagery of location (we don't really want the patient to have a map and start wandering around...)
    - Simple message
    - Confirmation and time that location was uploaded to server

**Limitations**
* Geolocation cannot happen if device's location services are not on.
* Geolocation on a website shouldn't happen on page load - user interaction via a button is recommended.
* If patient denies geolocation access to the web browser we cannot ask for it again - the patient then needs to revert that descision for the website manually on his device browser settings.

**What it is not**
* A search management tool
* A rescuer tracking tool
* A patient communication tool
* An incident logging tool

**Feature requests**
* Client side button to force update and location send
* CLient side data storage when reception is down and bulk upload
* Google earth to dashboard
* KMZ track/point export
* Mobile friendly map
* Zoom level on maps
* Scrolling table

**Costs and deploy limits**
* Heroku platform
* Heroku postgres
* Mapbox
* Google API
* w3w API
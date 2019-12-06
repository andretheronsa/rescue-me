RescueMe is an interactive dashboard to display current rescue data on a nice viewer

**Problem**
* People don't plane on being rescued
* Most phones are capable of accurate geolocation
* People generally don't have location apps on their phone and getting GPS coordinates is not that trivial
* Many people don't know how to share their location
* Location aware apps that can share location often do it in a specific format (wastsapp pin) that can't be entered into Heli/GPS etc.
* Reception in the mountains is poor - so downloading an app like what3words is not ideal
* Patients are typically in distress and unable to follow detailed phone instructions
* Patients are typically not experts in relying information and may mess up coordinate systems, lat/longs, decimal places etc.
* Nearly all phones have a browser with geolocation abilities

**Goal**
* To build a tool that:
    1. Retrieves accurate geolocation of the patient
    2. Runs with minimal user input
    3. Runs with minimal internet connectivity
    4. Is very lightweight
    5. Works on most internet connected devices
    6. 

**Solution**
* RescueMe browser tracking tool that runs in the cloud (app only spins up when accessed)
* Rescuer gets unique url from server and sends to patient
* Patient clicks link, presses a button to start monitoring and accepts location tracking (only input needed from patient side)
* Rescuers now have access to a map and table of patient data on the server including:
    - Latitude (decimal degrees rounded to 5 places (~1m) relative to WGS84)
    - Longitude (decimal degrees rounded to 5 places (~1m) relative to WGS84)
    - Position accuracy (meters)
    - Altitude (meters above the ellipsoid (~30m out in the cape))
    - Altidude accuracy (meters)
    - Speed (meters per second)
    - Heading (degrees)
    - User phone address (mac ID and IP)
    - Time since last call
* Geolocation updated as long as patient has site open
* Any authorized rescuer can view patient location and history
* App sends back basic info to patient
    - Location in decimal degrees
    - what2words location
    - Low resolution topographical map of location
    - Simple message
    - Confirmation and time that location was uploaded to server
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)

# Set routings
@app.route("/", methods=['GET', 'POST'])
def get_location():
    if request.method == 'POST':
        lat = request.args.get("latitude")
        lon = request.args.get("longitude")
    else:
        lat = lon = 0
    return render_template("get-location.html", lat = lat, lon = lon)

# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, ssl_context='adhoc')

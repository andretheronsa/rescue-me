from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)

# Set routings
@app.route("/", methods=['GET', 'POST'])
def get_location():
    if request.method == 'POST':
        lat = lon = request.args.get("latitude")
    else:
        lat = lon = 0
    return render_template("get-location.html", lat = lat, lon = lat)

# Run server
if __name__ == '__main__':
    app.run(debug=True)

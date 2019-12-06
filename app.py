from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)

# Login screen 
@app.route("/")
def index():
    pass
    return render_template("")

# Login screen 
@app.route("/login")
def login():
    return render_template("login.html")

# Generate a link for user
@app.route("/generate-link")
def generate_link():
    pass
    return render_template("")

# Main tracking routing
@app.route("/tracking", methods=['GET', 'POST'])
def get_location():
    if request.method == 'POST':
        lat = request.args.get("latitude")
        lon = request.args.get("longitude")
    else:
        lat = lon = 0
    return render_template("get-location.html", lat = lat, lon = lon)

# Monitor patients database and map
@app.route("/dashboard")
def dashboard():
    pass
    return render_template("")

# Run server
if __name__ == '__main__':
    app.run()

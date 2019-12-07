from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Init app
app = Flask(__name__)

# Init db
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Login screen 
@app.route("/")
def login():
    return render_template("login.html")

# Main tracking routing
@app.route("/tracking", methods=['GET', 'POST'])
def get_location():
    ip = request.remote_addr
    if request.method == "POST":
        data = request.get_json(force=True)
        print(type(data), data)
    return render_template("get-location.html", debug = ip)

# Monitor patients database and map
@app.route("/dashboard")
def dashboard():
    pass
    return render_template("")

# Run server
if __name__ == '__main__':
    app.run(debug=True)

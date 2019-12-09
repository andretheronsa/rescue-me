from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import os, sys

# Init app with DB and heroku
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)
GOOGLE_API=os.environ.get("GOOGLE_API")

# Main tracking routing
@app.route("/", methods=['GET', 'POST'])
def get_location():
    ip = request.remote_addr
    if request.method == "POST":
        data = request.get_json(force=True)
        try:
            db.session.add(data)
            db.session.commit()
            debug = "Succesfully commited to db"
        except Exception as e:
            print(e)
            sys.stdout.flush()
        print(type(data), data)
    return render_template("get-location.html", GOOGLE_API=GOOGLE_API, debug=ip)

# Login screen 
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('dashboard'))
    return render_template("login.html", error=error)

# Monitor patients database and map
@app.route("/dashboard")
def dashboard():
    pass
    return render_template("")

# Run server
if __name__ == '__main__':
    app.run(debug=True)

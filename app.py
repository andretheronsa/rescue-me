from flask import Flask, render_template, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import os

# Init app with DB and heroku
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

# Create db class
class Dataentry(db.Model):
    __tablename__ = "dataentry"
    id = db.Column(db.Integer, primary_key=True)
    mydata = db.Column(db.Text())

    def __init__ (self, mydata):
        self.mydata = mydata

# Main tracking routing
@app.route("/tracking", methods=['GET', 'POST'])
def get_location():
    ip = request.remote_addr
    if request.method == "POST":
        data = request.get_json(force=True)
        try:
            db.session.add(data)
            db.session.commit()
            debug = "Succesfully commited to db"
        except Exception as e:
            printData = copy(data. __dict__ )
            del data["_sa_instance_state"]
            print("\n FAILED entry: {}\n".format(json.dumps(printData)))
            print(e)
            sys.stdout.flush()
        print(type(data), data)
    return render_template("get-location.html", debug = ip)

# Login screen 
@app.route("/")
def login():
    return render_template("login.html")

# Monitor patients database and map
@app.route("/dashboard")
def dashboard():
    pass
    return render_template("")

# Run server
if __name__ == '__main__':
    app.run(debug=True)

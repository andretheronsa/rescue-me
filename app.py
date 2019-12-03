from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)

# Set routings
@app.route("/")
def get_location():
    return render_template("get-location.html")

# Run server
if __name__ == '__main__':
    app.run(debug=True)

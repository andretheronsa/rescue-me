from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)

# Init DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

# Create DB schema
class School(db.Model):
    __tablename__ = 'schools-geocoded'
    __table_args__ = { 'extend_existing': True }
    LOC_CODE = db.Column(db.Text, primary_key=True)

# Set routings
@app.route("/")
def get_location():
    return render_template("get-location.html")

# Run server
if __name__ == '__main__':
    app.run(debug=True)

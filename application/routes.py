import os, sys
from datetime import datetime as dt
import dateutil.parser as date_parser
from flask import render_template, request, jsonify, url_for, redirect, session, flash, send_from_directory
from flask_login import logout_user, login_user, current_user, login_required
from werkzeug.urls import url_parse
from flask import current_app as app
from application.models import db, User, Track, Location
from application.forms import LoginForm, Dashboard, Locate
import what3words

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static/favicon/'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route("/track-<track_id>", methods=['GET', 'POST'])
def locate(track_id):
    data={}
    # Ensure track ID has not expired yet
    track_time = dt.strptime(track_id, "%Y%m%d%H%M%S%f")
    current_time = dt.now()
    difference = current_time - track_time 
    if difference.days >= 3:
        allowed = "Sorry - track link expired (3 days max)"
        data["allowed"] = allowed
        return render_template("locate.html", data=data)
    # Ensure track ID has been issued
    exists = db.session.query(Track.track_name).filter_by(track_name=track_id).scalar() is not None
    if not exists:
        allowed="Sorry - track link not found"
        data["allowed"] = allowed
        return render_template("locate.html", data=data)
    # Recieve track data from client
    if request.method == "POST":
        # Parse position object return
        data = request.get_json(force=True)
        data["timestamp"] = date_parser.parse(data["timestamp"].split("(")[0])
        # Insert extra info about request
        data["ip"] = request.remote_addr
        data["track_id"] = track_id
        # find w3w location
        geocoder = what3words.Geocoder(app.config["W3W_API"])
        w3w = geocoder.convert_to_3wa(what3words.Coordinates(data["latitude"], data["longitude"]))
        data["w3w"] = w3w
        location = Location(**data)
        try:
            db.session.add(location)
            db.session.commit()
            data["info"] = "Succesfully uploaded user location measured at {} to db at: {}".format(data["timestamp"], dt.now())
        except Exception as e:
            print(e)
            sys.stdout.flush()
            data["info"] = "Location not yet uploaded to server"
            data["GOOGLE_API"]=app.config["GOOGLE_API"]
            data["allowed"]="true"
    return render_template("locate.html", data=data)

@app.route("/")
@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    # Create data object to send to html
    data = {}
    # Recieve post request for track data
    if request.method == 'POST':
        # Generate track id - based on exact time to be unique and useful
        share = request.get_json(force=True)
        track_id = dt.now().strftime("%Y%m%d%H%M%S%f")
        # Add track to the DB
        data = {"track_id": track_id,
                "share_team": share["share"],
                "user_id": current_user.id}
        track = Track(**data)
        try:
            db.session.add(track)
            db.session.commit()
            # Generate link to track url
            track_url="".join(request.url_root+'/track-'+track_id)
            data["track_url"] = track_url
        except Exception as e:
            print(e)
            sys.stdout.flush()
            track_url="Could not generate track URL"
    else:
        track_url="Generated track URL"
    data["GOOGLE_API"] = app.config["GOOGLE_API"]
    data["LATLON"] = "-33, 18"
    return render_template("dashboard.html", data=data)

# Logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

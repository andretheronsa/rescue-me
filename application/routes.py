import os, sys
from datetime import datetime as dt
import dateutil.parser as date_parser
from flask import render_template, request, jsonify, url_for, redirect, session, flash, send_from_directory
from flask_login import logout_user, login_user, current_user, login_required
from werkzeug.urls import url_parse
from flask import current_app as app
from application.models import db, User, Track, Location
from application.forms import LoginForm, DashboardForm, LocateForm, ShareForm
from application.tables import LocationTable, TrackTable
import what3words
import phonetic_alphabet as alpha
import string
from random import randint
from sqlalchemy import or_, not_

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static/favicon/'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def hello():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('share'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('share')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

#@app.route("/")
@app.route("/share", methods=['GET', 'POST'])
@login_required
def share():
    form = ShareForm()
    # Create data object to send to html
    data = {}
    # Recieve post request for track data
    if request.method == 'POST':
        # Generate track name - 3 character nato alphabet unique to tracking DB - 14k options
        share = form.share.data
        alias = form.alias.data
        exist = True
        while exist:
            name = "-".join(alpha.read(base(randint(676, 15624))).lower().split())
            exist = db.session.query(Track.id).filter_by(name=name).scalar() is not None
        url="".join(request.url_root+name)
        # Add track to the DB
        data = {"name": name,
                "alias": alias,
                "url": url,
                "share_team": share,
                "user_id": current_user.id}
        track = Track(**data)
        try:
            db.session.add(track)
            db.session.commit()
        except Exception as e:
            print(e)
            sys.stdout.flush()
            url="Could not generate track URL"
    else:
        url="Generated track URL"
    return render_template("share.html", url=url, title='Share', form=form)

@app.route("/<name>", methods=['GET', 'POST'])
def locate(name):
    data = False
    static_data = {"GOOGLE_API" : app.config["GOOGLE_API"], "url_valid" : True}
    # Ensure track ID has been issued
    exists = db.session.query(Track.name).filter_by(name=name).scalar() is not None
    if not exists:
        static_data["url_valid"] = False
    else:
        # Ensure track ID has not expired yet
        track_time = db.session.query(Track.create_time).filter_by(name=name).scalar()
        track_time_db = date_parser.parse(track_time.strftime('%c'))
        current_time = dt.now()
        difference = current_time - track_time_db 
        if difference.days >= 3:
            static_data["url_valid"] = False
    # Recieve track data from client
    if request.method == "POST":
        # Parse position object return
        data = request.get_json(force=True)
        data["timeStamp"] = date_parser.parse(data["timeStamp"].split("(")[0])
        # Insert extra info about request
        data["ip"] = request.remote_addr
        data["track_id"] = db.session.query(Track.id).filter_by(name=name)
        geocoder = what3words.Geocoder(app.config["W3W_API"])
        w3w = geocoder.convert_to_3wa(what3words.Coordinates(data["latitude"], data["longitude"]))
        data["w3w"] = w3w["words"]
        location_insert = Location(**data)
        try:
            db.session.add(location_insert)
            db.session.commit()
            static_data["info"] = "Succesfully uploaded user location measured at {} to db at: {}".format(data["timeStamp"], dt.now())
        except Exception as e:
            print(e)
            sys.stdout.flush()
            static_data["info"] = "Location not could not be uploaded to server"       
    return render_template("locate.html", title='Locate', static_data=static_data, data=data)

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    # Create data object to send to html
    allowed_track_items = Track.query.filter(or_(Track.user_id == current_user.id, Track.share_team == 1)).all()
    track_table = TrackTable(allowed_track_items)
    location_items = Location.query.filter().all()
    location_table = LocationTable(location_items)
    data = {"track_table": track_table, "location_table": location_table}
    data["GOOGLE_API"]=app.config["GOOGLE_API"]
    return render_template("dashboard.html", title='Dashboard', data = data)

# Logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Useful apps
def base(num,b=26,numerals="abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (base(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
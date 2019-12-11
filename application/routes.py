import os, sys
from datetime import datetime as dt
import dateutil.parser as date_parser
from flask import render_template, request, jsonify, url_for, redirect, session, flash
from flask_login import logout_user, login_user, current_user, login_required
from werkzeug.urls import url_parse
from flask import current_app as app
from application.models import db, User, Track, Location
from application.forms import LoginForm

@app.route("/tracking/<tracking_id>", methods=['GET', 'POST'])
def get_location(tracking_id):
    exists = db.session.query(Track.track_name).filter_by(track_name=tracking_id).scalar() is not None
    if not exists:
        return render_template("get-location.html", allowed="false")
    if request.method == "POST":
        data = request.get_json(force=True)
        data["timestamp"] = date_parser.parse(data["timestamp"].split("(")[0])
        data["ip"] = request.remote_addr
        data["track_id"] = tracking_id
        location = Location(**data)
        try:
            db.session.add(location)
            db.session.commit()
            debug = "Succesfully uploaded user location measured at {} to db at: {}".format(data["timestamp"], dt.now())
        except Exception as e:
            print(e)
            sys.stdout.flush()
            debug = "Location not yet uploaded to server"
    return render_template("get-location.html",
                           GOOGLE_API=app.config["GOOGLE_API"],
                           debug=debug,
                           allowed="true")

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
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        # Generate track id - based on exact time to be unique and useful
        share = request.get_json(force=True)
        track_id = dt.now().strftime("%Y%m%d%H%M%S%f").rstrip('0')
        # Add track to the DB
        data = {"track_id": track_id,
                "share_team": share["share"],
                "user_id": current_user.id}
        track = Track(**data)
        try:
            db.session.add(track)
            db.session.commit()
            # Generate link to tracking url
            tracking_url="".join(request.url_root+'/tracking/'+track_id)
        except Exception as e:
            print(e)
            sys.stdout.flush()
            tracking_url="Could not generate tracking URL"
    else:
        tracking_url="Generated tracking URL"
    return render_template("dashboard.html", tracking_url=tracking_url)

# Logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

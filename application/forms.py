from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators, SubmitField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional

class LoginForm(FlaskForm):
    """User Login Form."""

    username = StringField('Username', validators=[DataRequired('Please enter your username.')])
    password = PasswordField('Password', validators=[DataRequired('Please enter your password.')])
    submit = SubmitField('Log In')

class ShareForm(FlaskForm):
    """User Login Form."""
    share = BooleanField('Share with team')
    submit = SubmitField('Create tracking link')

class DashboardForm(FlaskForm):
    """Dashboard"""
    pass
    
class LocateForm(FlaskForm):
    """Tracking"""
    pass
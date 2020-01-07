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
    
    share = BooleanField('Allow team access', default="checked")
    alias = StringField('Link name', validators=[DataRequired('Unique name for tracking link')])
    submit = SubmitField('Create')
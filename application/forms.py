from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional

class LoginForm(FlaskForm):
    """User Login Form."""

    username = StringField('Username', validators=[DataRequired('Please enter your username.')])
    password = PasswordField('Password', validators=[DataRequired('Please enter your password.')])
    submit = SubmitField('Log In')
    
class Dashboard(FlaskForm):
    """User Login Form."""
    
class Locate(FlaskForm):
    """User Login Form."""
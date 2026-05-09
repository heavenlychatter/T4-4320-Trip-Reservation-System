from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

    username = StringField("Enter Username", [DataRequired()])

    password = PasswordField("Password", [DataRequired()])

    submit = SubmitField("Submit", )
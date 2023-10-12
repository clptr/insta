from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(db.Model):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=1)])
    submit = SubmitField("Log In")


class SignUpForm(db.Model):
    email = EmailField("Email", validators=[DataRequired(), Length(min=4, max=8)])
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    password_Confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Password does not match")])
    submit = SubmitField("Sign Up")


class EditProfile(db.Model):
    


class CreatePost(db.Model):
    pass


class EditPost(db.Model):
    pass


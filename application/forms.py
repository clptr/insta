from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(db.Model):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=1)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Log In")


class SignUpForm(db.Model):
    email = EmailField("Email", validators=[DataRequired(), Length(max=128)])
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    password_Confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Password does not match")])
    submit = SubmitField("Sign Up")


class EditProfile(db.Model):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=128)])
    bio = TextAreaField('Bio', validators=[Length(max=256)])
    profile_pic = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only (.jpg, .png)')])
    submit = SubmitField('Save Changes')



class CreatePost(db.Model):
    caption = TextAreaField('Caption', validators=[DataRequired(), Length(max=256)])
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'], 'Images only (.jpg, .png)')])
    submit = SubmitField('Add Post')


class EditPost(db.Model):
    caption = TextAreaField('Caption', validators=[DataRequired(), Length(max=256)])
    image = FileField('Edit Image', validators=[FileAllowed(['jpg', 'png'], 'Images only (.jpg, .png)')])
    submit = SubmitField('Save Changes')


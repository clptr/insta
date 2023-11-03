from flask_wtf import FlaskForm
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, EmailField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email

from application.utils import exists_email, not_exists_email, exists_username

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=1)])
    # remember_me = BooleanField('Remember Me')
    submit = SubmitField("Log In")


class SignUpForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(),Email(), exists_email])
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=12)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    fullname = StringField("Fullname", validators=[DataRequired(), Length(min=4, max=16)])
    password_Confirm = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=8), EqualTo("password", message="Password does not match")])
    submit = SubmitField("Sign Up")


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=12), exists_username])
    password = PasswordField("password", validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email(), exists_email])
    bio = StringField("Bio", validators=[Length(min=0)])
    profile_pic = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Save Changes')


class ResetPasswordForm(FlaskForm):
    old_password = PasswordField("old_password", validators=[DataRequired(), Length(min=8)])
    new_password = PasswordField("new_password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("new_password")])
    submit = SubmitField("Reset password")


class ForgotPasswordForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired(), not_exists_email])
    recaptcha = RecaptchaField()
    submit = SubmitField("send link verification to email")

class VerificationResetPasswordForm(FlaskForm):
    password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    password_Confirm = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit = SubmitField("reset password")


class CreatePostForm(FlaskForm):
    caption = TextAreaField('Caption')
    post_pic = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Add Post')


class EditPostForm(FlaskForm):
    caption = TextAreaField('Caption')
    # image = FileField('Edit Image')
    submit = SubmitField('Save Changes')


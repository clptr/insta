from wtforms.validators import ValidationError

from application import login_manager
from application.models import User


# FORM UTILS
def exists_email(form, email):
    user = User.query.filter_by(email = email.data).first()
    if user:
        raise ValidationError("email already exists. please use a different email.")

def not_exists_email(form, email):
    user = User.query.filter_by(email = email.data).first()
    if not user:
        raise ValidationError("email not found.")

def exists_username(form, username):
    user = User.query.filter_by(username = username.data).first()
    if user:
        raise ValidationError("username already exists. please use a different username")
# END OF FORM UTILS

# LOGIN MANAGER UTILS
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# END OF LOGIN MANAGER UTILS
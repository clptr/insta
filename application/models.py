from flask_login import UserMixin

from application import db
from datetime import datetime

class User(db.Model, UserMixin):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    profile_pic = db.Column(db.String(256), nullable=True)
    fullname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.String(256), nullable=True)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)
    following_user = db.relationship("Relation", db.ForeignKey"Relationship.following_id", backref="following", lazy=True)
    follower_user = db.relationship("Relation", db.ForeignKey"Relationship.follower_id", backref="follower", lazy=True)
    posts = db.relationship("Post", backref="posts_owner", lazy=True)
    comments = db.relationship("Comment", backref="comments_owner", lazy=True)
    likes = db.relationship("Like", backref="likes_owner", lazy=True)


class Relationship(db.Model):

    __tablename__ = "relationships"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=True)
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    relation_date = db.Column(db.DateTime, default=datetime.utcnow)


class Post(db.Model):

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256), nullable=False)
    caption = db.Column(db.String(256), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) 
    status = db.Column(db.Boolean, default=True)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow()) 
    comments = db.relationship("Comment", backref="commented", lazy=True)
    likes = db.relationship("Like", backref="liked", lazy=True)


class Comment(db.Model):

    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    commenter_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    text = db.Column(db.Text, nullable=False)
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)
    hidden = db.Column(db.Boolean, default=False)


class Like(db.Model):

    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    status = db.Column(db.Boolean, default=True)
    like_date = db.Column(db.DateTime, default=datetime.utcnow)

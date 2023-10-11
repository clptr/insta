from application import db
from datetime import datetime

class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    proimg = db.Column(db.String(256), nullable=True)
    name = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.String(256), nullable=True)
    relationships = db.relationship("Relationship", backref="user")
    posts = db.relationship("Post", backref="user")
    comments = db.relationship("Comment", backref="user")
    likes = db.relationship("Like", backref="user")

    def _repr_(self):
        return f"user: {self.username}"


class Relationship(db.Model):

    __tablename__ = "relationships"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(256))
    follower_id = db.Column(db.Integer, nullable=False)
    following_id = db.Column(db.Integer, nullable=False)


class Post(db.Model):

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256), nullable=False)
    caption = db.Column(db.String(256), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) 
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow()) 


class Comment(db.Model):

    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    text = db.Column(db.String(256), nullable=False)


class Like(db.Model):

    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)

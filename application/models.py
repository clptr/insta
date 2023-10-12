from application import db
from datetime import datetime

class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    proimg = db.Column(db.String(256), nullable=True)
    fullname = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.String(256), nullable=True)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)
    # relationships = db.relationship("Relationship", backref="user")
    # posts = db.relationship("Post", backref="user")
    # comments = db.relationship("Comment", backref="user")
    # likes = db.relationship("Like", backref="user")

    # def _repr_(self):
    #     return f"user: {self.username}"


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

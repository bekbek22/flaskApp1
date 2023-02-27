from app import db
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from datetime import datetime

class BlogEntry(db.Model, UserMixin, SerializerMixin):
    __tablename__ = "blog_entries"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer(), db.ForeignKey('auth_users.id'))
    avatar_url = db.Column(db.String(200))
    
    name = db.Column(db.String(50))
    message = db.Column(db.String(280))
    email = db.Column(db.String(50))
    datetime_created = db.Column(db.DateTime)
    datetime_updated = db.Column(db.DateTime)
    
    
    def __init__(self, name, message, email, owner_id, avatar_url):
        self.name = name
        self.message = message
        self.email = email
        self.datetime_created = datetime.now()
        self.datetime_updated = datetime.now()
        self.owner_id  = owner_id 
        self.avatar_url = avatar_url

    def update(self, name, message, email):
        self.name = name
        self.message = message
        self.email = email
        self.datetime_updated = datetime.now()

from uuid import uuid4
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(16), index=True, unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)


class MarketingLink(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(36), nullable=False)
    link = db.Column(db.String(64), default='')
    visits = db.Column(db.Integer(), default=0)

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Database models: Dette er overblik over hvilke typer objekter der gemmes i databasen og hvad de indeholder


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # Henter via func.now datetime dataen som bruges som timestamp
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # One to many relationsship - Ét object, med mange children (En user med mange notes)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    data = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# En user har altid et unikt ID - DB softwaren laver selv incremental på ID'et 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    files = db.relationship('File')

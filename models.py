from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

# Models.
#

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    genres = db.Column("genres", db.ARRAY(db.String()), nullable=False)
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(250))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(250))
    shows = db.relationship('show', backref=db.backref('venue'), lazy='joined')

    def __repr__(self):
      return f'<Venue {self.id} name: {self.name}>'


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    genres = db.Column("genres", db.ARRAY(db.String()), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('show', backref=db.backref('artist'), lazy='joined')

    def __repr__(self):
      return f'<Artist {self.id} name: {self.name}>'


class Show(db.Model):
    __tablename__ = 'show'

    id = db.Column(
      db.Integer,
      primary_key=True
    )

    artist_id = db.Column(
      db.Integer,
      db.ForeignKey('artist.id'),
      nullable=False
    )

    venue_id = db.Column(
      db.Integer,
      db.ForeignKey('venue.id'),
      nullable=False
    )

    start_time = db.Column(
      db.DateTime,
      nullable=False,
      default=datetime.utcnow
    )


    artist = db.relationship(
        'Artist', 
        backref=db.backref('shows_artist', cascade='all, delete'), 
        lazy='joined'
    )

    venue = db.relationship(
        'Venue', 
        backref=db.backref('shows_venue', cascade='all, delete'), 
        lazy='joined'
    )

    def __repr__(self):
      return f'<Show {self.id}, Artist {self.artist_id}, Venue {self.venue_id}>'

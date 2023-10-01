# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import CheckConstraint

#Create an SQLAlchemy instance.

db = SQLAlchemy()

#Create the hero table.

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    super_name = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    powers = db.relationship('Powers', secondary='hero_powers', back_populates='heroes')

#Create the powers table.

class Powers(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    heroes = db.relationship('Hero', secondary='hero_powers', back_populates='powers', lazy='dynamic')

    __table_args__ = (
        CheckConstraint(
            db.func.length(description) >= 20,
            name='description_length'
        ),
    )

#Create the hero_powers table

class Hero_Powers(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, unique=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    hero = db.relationship('Hero', backref='hero_powers')
    power = db.relationship('Powers', backref='hero_powers')

    __table_args__ = (
        CheckConstraint(
            strength.in_(['Strong', 'Weak', 'Average']),
            name='strength_values'
        ),
    )

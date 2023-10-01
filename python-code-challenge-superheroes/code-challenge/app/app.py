#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api


from models import db
from routes import HeroesResource, HeroResource, PowersResource, PowerResource, UpdatePowerResource, HeroPowersResource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
api=Api(app)

db.init_app(app)

@app.route('/')
def home():
    return 'THIS IS FLASK CODE-CHALLENGE RESTAURANTS.'

api.add_resource(HeroesResource, '/heroes')
api.add_resource(HeroResource, '/heroes/<int:id>')
api.add_resource(PowersResource, '/powers')
api.add_resource(PowerResource, '/powers/<int:id>')
api.add_resource(UpdatePowerResource, '/powers/<int:id>')
api.add_resource(HeroPowersResource, '/hero_powers')


if __name__ == '__main__':
    app.run(port=5555)

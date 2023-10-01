from flask import jsonify, request, abort
from models import db
from models import Hero, Powers, Hero_Powers
from flask_restful import Resource
#Get  all heroes.
class HeroesResource(Resource):
    def get(self):
        heroes = Hero.query.all()
        return jsonify([{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes])
    
#Get the heroes with id.
class HeroResource(Resource):
    def get(self, id):
        hero = Hero.query.get(id)
        if not hero:
            abort(404, error='Hero not found')
        powers = [{'id': power.id, 'name': power.name, 'description': power.description} for power in hero.powers]
        return jsonify({'id': hero.id, 'name': hero.name, 'super_name': hero.super_name, 'powers': powers})
    
#Get all the powers.
class PowersResource(Resource):
    def get(self):
        powers = Powers.query.all()
        return jsonify([{'id': power.id, 'name': power.name, 'description': power.description} for power in powers])
    
#Get all the powers with id.
class PowerResource(Resource):
    def get(self, id):
        power = Powers.query.get(id)
        if not power:
            abort(404, error='Power not found')
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
    
#perform patch on a particular resource.
class UpdatePowerResource(Resource):
    def patch(self, id):
        power = Powers.query.get(id)
        if not power:
            abort(404, error='Power not found')
        data = request.get_json()
        if 'description' not in data or len(data['description']) < 20:
            return {'errors': ['validation errors']}, 400
        power.description = data['description']
        db.session.commit()
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
    
#ADD DATA TO HERO POWERS TABLE.
class HeroPowersResource(Resource):
    def post(self):
        data = request.get_json()
        strength = data.get('strength')
        power_id = data.get('power_id')
        hero_id = data.get('hero_id')
        
        if not all([strength, power_id, hero_id]):
            return {'errors': ['validation errors']}, 400
        
        power = Powers.query.get(power_id)
        hero = Hero.query.get(hero_id)
        
        if not power or not hero:
            abort(404, error='Power or Hero not found')
        
        hero_power = Hero_Powers(strength=strength, hero=hero, power=power)
        db.session.add(hero_power)
        db.session.commit()
        
        return jsonify({'id': hero.id, 'name': hero.name, 'super_name': hero.super_name, 'powers': [{'id': power.id, 'name': power.name, 'description': power.description}]}), 201
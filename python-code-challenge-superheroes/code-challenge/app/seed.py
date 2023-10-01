# seed.py

from app import app, db
from models import Hero, Powers, Hero_Powers
from datetime import datetime

def seed_data():
    with app.app_context():
        # Create heroes
        superman = Hero(name='Superman', super_name='Clark Kent')
        batman = Hero(name='Batman', super_name='Bruce Wayne')
        db.session.add(superman)
        db.session.add(batman)
        
        # Create powers
        flight = Powers(name='Flight', description='Can fly')
        strength = Powers(name='Super Strength', description='Incredibly strong')
        db.session.add(flight)
        db.session.add(strength)
        
        # Assign powers to heroes
        hero_powers = [
            {'hero': superman, 'power': flight, 'strength': 'High'},
            {'hero': superman, 'power': strength, 'strength': 'Superhuman'},
            {'hero': batman, 'power': strength, 'strength': 'Peak human'},
        ]
        for data in hero_powers:
            hero_power = Hero_Powers(
                hero=data['hero'],
                power=data['power'],
                strength=data['strength']
            )
            db.session.add(hero_power)
        
        db.session.commit()

if __name__ == '__main__':
    seed_data()

from flask import Blueprint
from init import db
from datetime import datetime, UTC
from models.user import User


db_bp = Blueprint('db', __name__)


# Drop then create all tables
@db_bp.cli.command('init')
def create_tables():
    db.drop_all()
    db.create_all()
    print('Tables created.')
    

# Seed data
@db_bp.cli.command('init')
def create_tables():
    db.drop_all()
    db.create_all()
    print('Tables created.')
    
@db_bp.cli.command('seed')
def seed_tables():
    users = [
        User(
            id=1,
            username='SatoshiN',
            email='satoshi@bitcoin.org',
            country='Japan',
            created_at=datetime.now(UTC),
            is_active=True
        ),
        User(
            id=2,
            username='HodlKing',
            email='hodlking@moon.com',
            country='USA',
            is_active=True
        ),
        User(
            id=3,
            username='LightningMax',
            email='max@lightning.network',
            country='El Salvador'
        )
    ]
    
    db.session.add_all(users)
 
    db.session.commit()
    print('Tables seeded.')
from flask import Blueprint
from datetime import datetime, UTC

from init import db
from models.user import User
from models.cryptocurrency import Cryptocurrency
from models.fiatcurrency import FiatCurrency
from models.wallet import Wallet
from models.cryptoprice import CryptoPrice


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
    
    cryptocurrencies = [
        Cryptocurrency(
            id=1,
            name='Bitcoin',
            symbol='BTC'
        ),
        Cryptocurrency(
            id=2,
            name='Ethereum',
            symbol='ETH'
        ),
        Cryptocurrency(
            id=3,
            name='Solana',
            symbol='SOL'
        )
    ]
    
    db.session.add_all(cryptocurrencies)
 
    fiatcurrencies = [
        FiatCurrency(
            id=1,
            name='US Dollar',
            symbol='USD'
        ),
        FiatCurrency(
            id=2,
            name='Australian Dollar',
            symbol='AUD'
        ),
        FiatCurrency(
            id=3,
            name='Chinese Yuan',
            symbol='CNY'
        ),
        FiatCurrency(
            id=4,
            name='Euro',
            symbol='EUR'
        )
    ]
    
    db.session.add_all(fiatcurrencies)
    db.session.commit()
    
    wallets = [
        Wallet(
            user_id=1,
            crypto_id=1,
            amount=0.10000000
        ),
        Wallet(
            user_id=1,
            crypto_id=2,
            amount=0.20000000
        ),
        Wallet(
            user_id=2,
            crypto_id=2,
            amount=0.30000000
        ),
        Wallet(
            user_id=2,
            crypto_id=3,
            amount=0.40000000
        ),
        Wallet(
            user_id=3,
            crypto_id=3,
            amount=0.50000000
        ),
        Wallet(
            user_id=3,
            crypto_id=1,
            amount=0.60000000
        )
    ]
 
    db.session.add_all(wallets)
    
    cryptoprices = [
        CryptoPrice(
            amount=84610,
            price_updated="2025-03-21T15:25:56.000000",
            crypto_id=1,
            fiat_id=1
        )
    ]
 
    db.session.add_all(cryptoprices)
    
    db.session.commit()
    print('Tables seeded.')
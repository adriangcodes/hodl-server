from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
import psycopg2

from init import db
from models.cryptocurrency import Cryptocurrency, many_cryptocurrencies, one_cryptocurrency, CryptocurrencySchema, cryptocurrency_without_id


cryptocurrencies_bp = Blueprint('cryptocurrencies', __name__)


# Create
@cryptocurrencies_bp.route('/cryptocurrencies', methods=['POST'])
def create_crypto():
    try:
        # Get incoming request body (JSON)
        data = cryptocurrency_without_id.load(request.json)
        # Create new instance of Cryptocurrency model
        new_cryptocurrency = Cryptocurrency(
            name = data['name'],
            symbol = data['symbol']
        )
        # Add the instance to the db session
        db.session.add(new_cryptocurrency)
        # Commit the instance to the db
        db.session.commit()
        return one_cryptocurrency.dump(new_cryptocurrency), 201
    
    except IntegrityError as err:
        # Rollback on error
        db.session.rollback()  
        if isinstance(err.orig, psycopg2.errors.UniqueViolation):
            return {"error": "A cryptocurrency with this name or symbol already exists."}, 400
        elif isinstance(err.orig, psycopg2.errors.NotNullViolation):
            return {"error": "A required field is missing."}, 400
        else:
            return {"error": f"Database constraint violated: {str(err.orig)}"}, 400
    
    except Exception as err:
        return {"error": str(err)}, 400


# Read - One
@cryptocurrencies_bp.route('/cryptocurrencies/<int:crypto_id>')
def get_one_crypto(crypto_id):
    stmt = db.select(Cryptocurrency).filter_by(id=crypto_id)
    cryptocurrency = db.session.scalar(stmt)
    if cryptocurrency:
        return one_cryptocurrency.dump(cryptocurrency)
    else:
        return {"error": f"Cryptocurrency with id {crypto_id} not found."}, 404


# Read - All
@cryptocurrencies_bp.route('/cryptocurrencies')
def get_all_cryptos():
    stmt = db.select(Cryptocurrency).order_by(Cryptocurrency.id.asc()) # Orders by ascending id
    cryptocurrencies = db.session.scalars(stmt)
    return many_cryptocurrencies.dump(cryptocurrencies)


# Update
@cryptocurrencies_bp.route('/cryptocurrencies/<int:crypto_id>', methods=['PUT', 'PATCH'])
def update_crypto(crypto_id):
    try:
        # Fetch cryptocurrency by id
        stmt = db.select(Cryptocurrency).filter_by(id=crypto_id)
        cryptocurrency = db.session.scalar(stmt)
        if cryptocurrency:
            # Get incoming request body (JSON)
            data = cryptocurrency_without_id.load(request.json, partial=True)
            # Update the attributes of the cryptocurrency with the incoming data - OR option covers both PUT and PATCH methods
            cryptocurrency.name = data.get('name') or cryptocurrency.name
            cryptocurrency.symbol = data.get('symbol') or cryptocurrency.symbol
            # Commit the instance to the db
            db.session.commit()
            return one_cryptocurrency.dump(cryptocurrency), 200
        else:
            return {"error": f"Cryptocurrency with id {crypto_id} not found."}, 404
    
    except Exception as err:
        return {"error": str(err)}, 400


# Delete
@cryptocurrencies_bp.route('/cryptocurrencies/<int:crypto_id>', methods=['DELETE'])
def delete_crypto(crypto_id):
    stmt = db.select(Cryptocurrency).filter_by(id=crypto_id)
    cryptocurrency = db.session.scalar(stmt)
    if cryptocurrency:
        db.session.delete(cryptocurrency)
        db.session.commit()
        return {}, 204
    else:
        return {"error": f"Cryptocurrency with id {crypto_id} not found."}, 404
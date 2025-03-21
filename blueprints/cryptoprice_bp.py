from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from datetime import datetime, UTC
import psycopg2

from init import db
from models.cryptoprice import CryptoPrice, many_cryptoprices, one_cryptoprice, CryptoPriceSchema, cryptoprice_without_id


cryptoprices_bp = Blueprint('cryptoprices', __name__)


# Create
@cryptoprices_bp.route('/cryptoprices', methods=['POST'])
def create_cryptoprice():
    try:
        # Get incoming request body (JSON)
        data = cryptoprice_without_id.load(request.json)
        # Create new instance of CryptoPrice model
        new_cryptoprice = CryptoPrice(
            amount = data['amount'],
            price_updated = data.get('created_at', datetime.now(UTC)),
            crypto_id = data['crypto_id'],
            fiat_id = data['fiat_id'],
        )
        # Add the instance to the db session
        db.session.add(new_cryptoprice)
        # Commit the instance to the db
        db.session.commit()
        return one_cryptoprice.dump(new_cryptoprice), 201
    
    except IntegrityError as err:
        # Rollback on error
        db.session.rollback()  
        if isinstance(err.orig, psycopg2.errors.NotNullViolation):
            return {"error": "A required field is missing."}, 400
        else:
            return {"error": f"Database constraint violated: {str(err.orig)}"}, 400
    
    except Exception as err:
        return {"error": str(err)}, 400


# Read - One
@cryptoprices_bp.route('/cryptoprices/<int:price_id>')
def get_one_cryptoprice(price_id):
    stmt = db.select(CryptoPrice).filter_by(id=price_id)
    cryptoprice = db.session.scalar(stmt)
    if cryptoprice:
        return one_cryptoprice.dump(cryptoprice)
    else:
        return {"error": f"Price record with id {price_id} not found."}, 404


# Read - All
@cryptoprices_bp.route('/cryptoprices')
def get_all_cryptoprices():
    stmt = db.select(CryptoPrice).order_by(CryptoPrice.id.asc()) # Orders by ascending id
    cryptoprices = db.session.scalars(stmt)
    return many_cryptoprices.dump(cryptoprices)


# Update
@cryptoprices_bp.route('/cryptoprices/<int:price_id>', methods=['PUT', 'PATCH'])
def update_cryptoprice(price_id):
    try:
        # Fetch price record by id
        stmt = db.select(CryptoPrice).filter_by(id=price_id)
        cryptoprice = db.session.scalar(stmt)
        if cryptoprice:
            # Get incoming request body (JSON)
            data = cryptoprice_without_id.load(request.json, partial=True)
            # Update the attributes of the price record with the incoming data - OR option covers both PUT and PATCH methods
            cryptoprice.amount = data.get('amount') or cryptoprice.amount
            cryptoprice.price_updated = data.get('price_updated') or cryptoprice.price_updated
            cryptoprice.crypto_id = data.get('crypto_id') or cryptoprice.crypto_id
            cryptoprice.fiat_id = data.get('fiat_id') or cryptoprice.fiat_id
            # Commit the instance to the db
            db.session.commit()
            return one_cryptoprice.dump(cryptoprice), 200
        else:
            return {"error": f"Price record with id {price_id} not found."}, 404
    
    except Exception as err:
        return {"error": str(err)}, 400


# Delete
@cryptoprices_bp.route('/cryptoprices/<int:price_id>', methods=['DELETE'])
def delete_cryptoprice(price_id):
    stmt = db.select(CryptoPrice).filter_by(id=price_id)
    cryptoprice = db.session.scalar(stmt)
    if cryptoprice:
        db.session.delete(cryptoprice)
        db.session.commit()
        return {}, 204
    else:
        return {"error": f"CryptoPrice with id {price_id} not found."}, 404
from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
import psycopg2

from init import db
from models.fiatcurrency import FiatCurrency, many_fiatcurrencies, one_fiatcurrency, FiatCurrenciesSchema, fiatcurrency_without_id


fiatcurrencies_bp = Blueprint('fiatcurrencies', __name__)


# Create
@fiatcurrencies_bp.route('/fiatcurrencies', methods=['POST'])
def create_fiat():
    try:
        # Get incoming request body (JSON)
        data = fiatcurrency_without_id.load(request.json)
        # Create new instance of FiatCurrency model
        new_fiatcurrency = FiatCurrency(
            name = data['name'],
            symbol = data['symbol']
        )
        # Add the instance to the db session
        db.session.add(new_fiatcurrency)
        # Commit the instance to the db
        db.session.commit()
        return one_fiatcurrency.dump(new_fiatcurrency), 201
    
    except IntegrityError as err:
        # Rollback on error
        db.session.rollback()  
        if isinstance(err.orig, psycopg2.errors.UniqueViolation):
            return {"error": "A Fiat Currency with this name or symbol already exists."}, 400
        elif isinstance(err.orig, psycopg2.errors.NotNullViolation):
            return {"error": "A required field is missing."}, 400
        else:
            return {"error": f"Database constraint violated: {str(err.orig)}"}, 400
    
    except Exception as err:
        return {"error": str(err)}, 400


# Read - One
@fiatcurrencies_bp.route('/fiatcurrencies/<int:fiat_id>')
def get_one_fiat(fiat_id):
    stmt = db.select(FiatCurrency).filter_by(id=fiat_id)
    fiatcurrency = db.session.scalar(stmt)
    if fiatcurrency:
        return one_fiatcurrency.dump(fiatcurrency)
    else:
        return {"error": f"Fiat Currency with id {fiat_id} not found."}, 404


# Read - All
@fiatcurrencies_bp.route('/fiatcurrencies')
def get_all_fiats():
    stmt = db.select(FiatCurrency).order_by(FiatCurrency.id.asc()) # Orders by ascending id
    fiatcurrencies = db.session.scalars(stmt)
    return many_fiatcurrencies.dump(fiatcurrencies)


# Update
@fiatcurrencies_bp.route('/fiatcurrencies/<int:fiat_id>', methods=['PUT', 'PATCH'])
def update_fiat(fiat_id):
    try:
        # Fetch fiat currency by id
        stmt = db.select(FiatCurrency).filter_by(id=fiat_id)
        fiatcurrency = db.session.scalar(stmt)
        if fiatcurrency:
            # Get incoming request body (JSON)
            data = fiatcurrency_without_id.load(request.json, partial=True)
            # Update the attributes of the fiat currency with the incoming data - OR option covers both PUT and PATCH methods
            fiatcurrency.name = data.get('name') or fiatcurrency.name
            fiatcurrency.symbol = data.get('symbol') or fiatcurrency.symbol
            # Commit the instance to the db
            db.session.commit()
            return one_fiatcurrency.dump(fiatcurrency), 200
        else:
            return {"error": f"Fiat Currency with id {fiat_id} not found."}, 404
    
    except Exception as err:
        return {"error": str(err)}, 400


# Delete
@fiatcurrencies_bp.route('/fiatcurrencies/<int:fiat_id>', methods=['DELETE'])
def delete_fiat(fiat_id):
    stmt = db.select(FiatCurrency).filter_by(id=fiat_id)
    fiatcurrency = db.session.scalar(stmt)
    if fiatcurrency:
        db.session.delete(fiatcurrency)
        db.session.commit()
        return {}, 204
    else:
        return {"error": f"Fiat Currency with id {fiat_id} not found."}, 404
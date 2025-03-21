from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from datetime import datetime, UTC
import psycopg2

from init import db
from models.wallet import Wallet, many_wallets, one_wallet, WalletSchema, wallet_without_id


wallets_bp = Blueprint('wallets', __name__)


# Create
@wallets_bp.route('/wallets', methods=['POST'])
def create_wallet():
    try:
        # Get incoming request body (JSON)
        data = wallet_without_id.load(request.json)
        # Create new instance of Wallet model
        new_wallet = Wallet(
            amount = data.get('amount', 0.00000000),
            last_updated = data.get('created_at', datetime.now(UTC)),
            user_id = data['user_id'],
            crypto_id = data['crypto_id']
        )
        # Add the instance to the db session
        db.session.add(new_wallet)
        # Commit the instance to the db
        db.session.commit()
        return one_wallet.dump(new_wallet), 201
    
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
@wallets_bp.route('/wallets/<int:wallet_id>')
def get_one_wallet(wallet_id):
    stmt = db.select(Wallet).filter_by(id=wallet_id)
    wallet = db.session.scalar(stmt)
    if wallet:
        return one_wallet.dump(wallet)
    else:
        return {"error": f"Wallet with id {wallet_id} not found."}, 404


# Read - All
@wallets_bp.route('/wallets')
def get_all_wallets():
    stmt = db.select(Wallet).order_by(Wallet.id.asc()) # Orders by ascending id
    wallets = db.session.scalars(stmt)
    return many_wallets.dump(wallets)


# Update
@wallets_bp.route('/wallets/<int:wallet_id>', methods=['PUT', 'PATCH'])
def update_wallet(wallet_id):
    try:
        # Fetch wallet by id
        stmt = db.select(Wallet).filter_by(id=wallet_id)
        wallet = db.session.scalar(stmt)
        if wallet:
            # Get incoming request body (JSON)
            data = wallet_without_id.load(request.json, partial=True)
            # Update the attributes of the wallet with the incoming data - OR option covers both PUT and PATCH methods
            wallet.amount = data.get('amount') or wallet.amount
            wallet.last_updated = data.get('last_updated') or wallet.last_updated
            wallet.user_id = data.get('user_id') or wallet.user_id
            wallet.crypto_id = data.get('crypto_id') or wallet.crypto_id
            # Commit the instance to the db
            db.session.commit()
            return one_wallet.dump(wallet), 200
        else:
            return {"error": f"Wallet with id {wallet_id} not found."}, 404
    
    except Exception as err:
        return {"error": str(err)}, 400


# Delete
@wallets_bp.route('/wallets/<int:wallet_id>', methods=['DELETE'])
def delete_wallet(wallet_id):
    stmt = db.select(Wallet).filter_by(id=wallet_id)
    wallet = db.session.scalar(stmt)
    if wallet:
        db.session.delete(wallet)
        db.session.commit()
        return {}, 204
    else:
        return {"error": f"Wallet with id {wallet_id} not found."}, 404
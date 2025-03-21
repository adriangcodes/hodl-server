from init import db, ma
from marshmallow_sqlalchemy import fields
from datetime import datetime, UTC
from marshmallow import fields
from marshmallow.validate import Email, Regexp, Range
from sqlalchemy import Numeric
from decimal import Decimal


class Wallet(db.Model):
    __tablename__ = 'wallets'
    
    id = db.Column(db.Integer, primary_key=True)
    
    amount = db.Column(db.Numeric(65,8), default=0.00000000)
    last_updated = db.Column(db.DateTime, default=datetime.now(UTC))
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    crypto_id = db.Column(db.Integer, db.ForeignKey('cryptocurrencies.id'))
    

class WalletSchema(ma.Schema):
    amount = fields.Decimal(required=True, validate=Range(min=Decimal("0.0"), error="Wallet amount cannot be less than zero."))
    last_updated = fields.DateTime(error="Value must be a DateTime format.")

    class Meta:
        fields = ('id', 'amount', 'last_updated', 'user_id', 'crypto_id')
        

one_wallet = WalletSchema()
many_wallets = WalletSchema(many=True)
wallet_without_id = WalletSchema(exclude=['id'])
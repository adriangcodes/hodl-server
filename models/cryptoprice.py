from marshmallow_sqlalchemy import fields
from datetime import datetime, UTC
from marshmallow import fields
from marshmallow.validate import Range

from init import db, ma


class CryptoPrice(db.Model):
    __tablename__ = 'cryptoprices'
    
    id = db.Column(db.Integer, primary_key=True)
    
    amount = db.Column(db.Numeric(65,2), default=0.00)
    price_updated = db.Column(db.DateTime, default=datetime.now(UTC))
    
    crypto_id = db.Column(db.Integer, db.ForeignKey('cryptocurrencies.id'))
    fiat_id = db.Column(db.Integer, db.ForeignKey('fiatcurrencies.id'))

    fiatcurrency = db.relationship('FiatCurrency')
    cryptocurrency = db.relationship('Cryptocurrency')


class CryptoPriceSchema(ma.Schema):
    amount = fields.Decimal(as_string=True, places=2, validate=Range(min=0), error_messages={'invalid': 'Amount must be a number with up to 2 decimal places.', 'invalid_range': 'Amount must be a positive number.'})
    price_updated = fields.DateTime(error="Value must be a DateTime format.")
    
    fiatcurrency = fields.Nested('FiatCurrencySchema', exclude=['id'])
    cryptocurrency = fields.Nested('CryptocurrencySchema', exclude=['id'])
    
    class Meta:
        fields = ('id', 'amount', 'price_updated', 'crypto_id', 'cryptocurrency', 'fiat_id', 'fiatcurrency')
        

one_cryptoprice = CryptoPriceSchema()
many_cryptoprices = CryptoPriceSchema(many=True)
cryptoprice_without_id = CryptoPriceSchema(exclude=['id'])
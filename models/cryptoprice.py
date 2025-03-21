from marshmallow_sqlalchemy import fields
from datetime import datetime, UTC
from marshmallow import fields

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
    last_updated = fields.DateTime(error="Value must be a DateTime format.")
    
    fiatcurrency = fields.Nested('FiatCurrencySchema', exclude=['id'])
    cryptocurrency = fields.Nested('CryptocurrencySchema', exclude=['id'])
    
    class Meta:
        fields = ('id', 'amount', 'price_updated', 'crypto_id', 'cryptocurrency', 'fiat_id', 'fiatcurrency')
        

one_cryptoprice = CryptoPriceSchema()
many_cryptoprices = CryptoPriceSchema(many=True)
cryptoprice_without_id = CryptoPriceSchema(exclude=['id'])
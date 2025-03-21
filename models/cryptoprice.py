from init import db, ma
from marshmallow_sqlalchemy import fields
from datetime import datetime, UTC
from marshmallow import fields


class CryptoPrice(db.Model):
    __tablename__ = 'cryptoprices'
    
    id = db.Column(db.Integer, primary_key=True)
    
    amount = db.Column(db.Numeric(65,2), default=0.00)
    price_updated = db.Column(db.DateTime, default=datetime.now(UTC))
    
    crypto_id = db.Column(db.Integer, db.ForeignKey('cryptocurrencies.id'))
    fiat_id = db.Column(db.Integer, db.ForeignKey('fiatcurrencies.id'))


class CryptoPriceSchema(ma.Schema):
    last_updated = fields.DateTime(error="Value must be a DateTime format.")
    class Meta:
        fields = ('id', 'amount', 'price_updated', 'crypto_id', 'fiat_id')
        

one_cryptoprice = CryptoPriceSchema()
many_cryptoprices = CryptoPriceSchema(many=True)
cryptoprice_without_id = CryptoPriceSchema(exclude=['id'])
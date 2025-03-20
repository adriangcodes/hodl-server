from init import db, ma
from marshmallow_sqlalchemy import fields
from datetime import datetime, UTC
from marshmallow import fields
from marshmallow.validate import Regexp


class Cryptocurrency(db.Model):
    __tablename__ = 'cryptocurrencies'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    

class CryptocurrencySchema(ma.Schema):
    name = fields.String(required=True, validate=Regexp(r'^[a-zA-Z]+$', error="Name must contain letters only."))
    symbol = fields.String(required=True, validate=Regexp(r'^[A-Z]+$', error="Symbol must contain upper case letters only."))

    class Meta:
        fields = ('id', 'name', 'symbol')
        

one_cryptocurrency = CryptocurrencySchema()
many_cryptocurrencies = CryptocurrencySchema(many=True)
cryptocurrency_without_id = CryptocurrencySchema(exclude=['id'])
from marshmallow_sqlalchemy import fields
from marshmallow import fields
from marshmallow.validate import Regexp

from init import db, ma


class FiatCurrency(db.Model):
    __tablename__ = 'fiatcurrencies'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    

class FiatCurrencySchema(ma.Schema):
    name = fields.String(required=True, validate=Regexp(r'^[a-zA-Z ]+$', error="Name must contain letters and spaces only."))
    symbol = fields.String(required=True, validate=Regexp(r'^[A-Z]+$', error="Symbol must contain upper case letters only."))

    class Meta:
        fields = ('id', 'name', 'symbol')
        

one_fiatcurrency = FiatCurrencySchema()
many_fiatcurrencies = FiatCurrencySchema(many=True)
fiatcurrency_without_id = FiatCurrencySchema(exclude=['id'])
from init import db, ma
from marshmallow_sqlalchemy import fields
from marshmallow import fields
from marshmallow.validate import Regexp


class FiatCurrency(db.Model):
    __tablename__ = 'fiatcurrencies'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    

class FiatCurrenciesSchema(ma.Schema):
    name = fields.String(required=True, validate=Regexp(r'^[a-zA-Z ]+$', error="Name must contain letters and spaces only."))
    symbol = fields.String(required=True, validate=Regexp(r'^[A-Z]+$', error="Symbol must contain upper case letters only."))

    class Meta:
        fields = ('id', 'name', 'symbol')
        

one_fiatcurrency = FiatCurrenciesSchema()
many_fiatcurrencies = FiatCurrenciesSchema(many=True)
fiatcurrency_without_id = FiatCurrenciesSchema(exclude=['id'])
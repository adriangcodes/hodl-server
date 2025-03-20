from init import db, ma
from marshmallow_sqlalchemy import fields
from datetime import datetime, UTC
from marshmallow import fields
from marshmallow.validate import Email, Regexp


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.now(UTC))
    is_active = db.Column(db.Boolean, default=True)
    

class UserSchema(ma.Schema):
    username = fields.String(required=True, validate=Regexp(r'^[a-zA-Z0-9]+$', error="Username must contain only letters and numbers."))
    email = fields.Email(required=True, error_messages={"Invalid": "Invalid email address."})
    country = fields.String(required=True, validate=Regexp(r'^[a-zA-Z]+$', error="Country must contain only letters."))
    created_at = fields.DateTime(required=True, error="Value must be a DateTime format.")
    is_active = fields.Boolean(required=True, error="Value is either True or False.")
    class Meta:
        fields = ('id', 'username', 'email', 'country', 'created_at', 'is_active')
        

one_user = UserSchema()
many_users = UserSchema(many=True)
user_without_id = UserSchema(exclude=['id'])
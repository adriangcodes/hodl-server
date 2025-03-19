from init import db, ma
from marshmallow_sqlalchemy import fields
from datetime import datetime, UTC
# from marshmallow import fields # Required for .String validation
# from marshmallow.validate import Length, And, Regexp # Required for Length validation


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.now(UTC))
    is_active = db.Column(db.Boolean, default=True)
    

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'country', 'created_at', 'is_active')
        

one_user = UserSchema()
many_users = UserSchema(many=True)
user_without_id = UserSchema(exclude=['id'])
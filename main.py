from flask import Flask
from init import db, ma
from dotenv import load_dotenv
from marshmallow.exceptions import ValidationError
import os
from blueprints.db_bp import db_bp
from blueprints.users_bp import users_bp

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    
    # Global validation error handling
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"Error": "Invalid input."}, 400
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(db_bp)
    app.register_blueprint(users_bp)
    
    return app
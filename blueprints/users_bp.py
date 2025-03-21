from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from datetime import datetime, UTC
import psycopg2

from init import db
from models.user import User, many_users, one_user, UserSchema, user_without_id


users_bp = Blueprint('users', __name__)


# Create
@users_bp.route('/users', methods=['POST'])
def create_user():
    try:
        # Get incoming request body (JSON)
        data = user_without_id.load(request.json)
        # Create new instance of User model
        new_user = User(
            username = data['username'],
            email = data['email'],
            country = data['country'],
            created_at = data.get('created_at', datetime.now(UTC)),
            is_active = data.get('is_active', True)
        )
        # Add the instance to the db session
        db.session.add(new_user)
        # Commit the instance to the db
        db.session.commit()
        return one_user.dump(new_user), 201
    
    except IntegrityError as err:
        # Rollback on error
        db.session.rollback()  
        if isinstance(err.orig, psycopg2.errors.UniqueViolation):
            return {"error": "A user with this username or email already exists."}, 400
        elif isinstance(err.orig, psycopg2.errors.NotNullViolation):
            return {"error": "A required field is missing."}, 400
        else:
            return {"error": f"Database constraint violated: {str(err.orig)}"}, 400
    
    except Exception as err:
        return {"error": str(err)}, 400


# Read - One
@users_bp.route('/users/<int:user_id>')
def get_one_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        return one_user.dump(user)
    else:
        return {"error": f"User with id {user_id} not found."}, 404


# Read - All
@users_bp.route('/users')
def get_all_users():
    stmt = db.select(User).order_by(User.id.asc()) # Orders by ascending id
    users = db.session.scalars(stmt)
    return many_users.dump(users)


# Update
@users_bp.route('/users/<int:user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    try:
        # Fetch user by id
        stmt = db.select(User).filter_by(id=user_id)
        user = db.session.scalar(stmt)
        if user:
            # Get incoming request body (JSON)
            data = user_without_id.load(request.json, partial=True)
            # Update the attributes of the user with the incoming data - OR option covers both PUT and PATCH methods
            user.username = data.get('username') or user.username
            user.email = data.get('email') or user.email
            user.country = data.get('country') or user.country
            user.created_at = data.get('created_at') or user.created_at
            user.is_active = data.get('is_active') or user.is_active
            # Commit the instance to the db
            db.session.commit()
            return one_user.dump(user), 200
        else:
            return {"error": f"User with id {user_id} not found."}, 404
    
    except Exception as err:
        return {"error": str(err)}, 400


# Delete
@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {}, 204
    else:
        return {"error": f"User with id {user_id} not found."}, 404
"""Database models for the application."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    """Represents a user in the system."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128))
    address = db.Column(db.String(128))

    @classmethod
    def all(cls):
        """Retrieve all user records."""
        return cls.query.all()

    @classmethod
    def find_user_by_name(cls, user_name):
        """Find a user by their name."""
        return cls.query.filter(cls.name == user_name).first()

    @classmethod
    def find_user_by_email(cls, user_email):
        """Find a user by their email."""
        return cls.query.filter(cls.email == user_email).first()

    @classmethod
    def find_user_by_id(cls, user_id):
        """Find a user by their unique ID."""
        return cls.query.filter(cls.id == user_id).first()

    @classmethod
    def record_count(cls):
        """Return the total count of users."""
        return cls.query.count()

"""Configuration settings for the Flask application."""

import os

class Config:
    """Application configuration class."""

    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "TRUE")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///app.db")

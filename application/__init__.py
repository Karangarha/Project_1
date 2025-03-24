"""Main application initialization module."""

from flask import Flask
from flask_migrate import Migrate
import config
from application.database import db
from application.bp.homepage import homepage

# Initialize Flask-Migrate
migrate = Migrate()

def init_app():
    """Initialize the Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config())

    # Initialize database and migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    with app.app_context():
        app.register_blueprint(homepage)

    return app

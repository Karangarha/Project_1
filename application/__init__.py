
from flask import Flask
from flask_migrate import Migrate

from application.bp.homepage import homepage
import config
from application.database import db

migrate = Migrate()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config())

    db.init_app(app)
    migrate.init_app(app,db)

    with app.app_context():
        app.register_blueprint(homepage)
        return app





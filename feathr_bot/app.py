import logging
import os
from flask import Flask
from feathr_bot import routes
from feathr_bot.extensions import cors, db, marshmallow, migrate


def create_app(context: str = "") -> Flask:
    """Create application factory."""

    app = Flask(__name__)

    if context.lower() == "testing":
        app.config.from_pyfile("config.test.py")
    else:
        app.config.from_pyfile("config.py")

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask) -> None:
    """Register Flask extensions."""
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    return None


def register_blueprints(app: Flask) -> None:
    """Register Flask blueprints."""
    app.register_blueprint(routes.errors.blueprint)
    app.register_blueprint(routes.analyze.blueprint)
    app.register_blueprint(routes.chat.blueprint)
    return None

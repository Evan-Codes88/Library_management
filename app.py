from flask import Flask
import os

from controllers.cli_controller import db_commands
from controllers.author_controller import authors_bp
from controllers.genre_controller import genres_bp
from controllers.member_controller import members_bp
from init import db, ma


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")

    app.json.sort_keys = False

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(authors_bp)
    app.register_blueprint(genres_bp)
    app.register_blueprint(members_bp)

    return app
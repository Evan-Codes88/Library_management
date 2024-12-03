from flask import Flask
import os

from init import db, ma

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_UI")

    db.init_app(app)
    ma.init_app(app)

    return app
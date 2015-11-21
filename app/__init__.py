from flask import Flask
from config import Config
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.config["MONGODB_SETTINGS"] = {'DB': "MMCS_survey"}
    app.config["SECRET_KEY"] = ""

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

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

    from .survey import survey as survey_blueprint
    app.register_blueprint(survey_blueprint,  url_prefix='/survey')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .maintaining import maintaining as maintaining_blueprint
    app.register_blueprint(maintaining_blueprint, url_prefix='/maintaining')

    return app

from flask import Flask
from config import Config
from flask.ext.mongoengine import MongoEngine


# def create_app():
#     app = Flask(__name__)
#     app.config["MONGODB_SETTINGS"] = {'DB': "MMCS_survey", 'alias':'default', host='localhost'}
#     app.config["SECRET_KEY"] = ""
#     db = MongoEngine().connection
#

#
#     return app, db
#
# app, db = create_app()

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "MMCS_survey", 'alias':'default', 'host':'localhost'}
app.config["SECRET_KEY"] = ""
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .survey import survey as survey_blueprint
app.register_blueprint(survey_blueprint,  url_prefix='/survey')
db = MongoEngine(app)





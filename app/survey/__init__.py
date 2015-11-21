from flask import Blueprint

survey = Blueprint('survey', __name__)

from . import views
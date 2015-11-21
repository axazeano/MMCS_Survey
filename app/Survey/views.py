from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from model import BasicSurvey

survey = Blueprint('survey',  __name__, template_folder='templates')


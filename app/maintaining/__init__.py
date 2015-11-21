from flask import Blueprint

maintaining = Blueprint('maintaining', __name__)

from . import views
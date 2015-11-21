from flask import render_template
from . import survey


@survey.route('/')
def index():
    return render_template("survey/index.html")


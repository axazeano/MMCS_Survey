from flask import render_template
from . import auth


@auth.route('/login')
def index():
    return render_template("survey/index.html")


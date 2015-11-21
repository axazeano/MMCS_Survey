from flask import render_template
from . import maintaining


@maintaining.route('/maintaining')
def index():
    return render_template("maintaining.html")
from flask import Flask
from flask import render_template
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)


app.config["MONGODB_SETTINGS"] = {'DB': "MMCS_survey"}
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = ""

db = MongoEngine(app)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

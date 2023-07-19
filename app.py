from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

{}

@app.get('/')
def to_homepage():
    name = request.args['noun']

    return render_template(
        "questions.html",

    )
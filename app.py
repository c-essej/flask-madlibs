from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)



# ["place", "noun", "verb", "adjective", "plural_noun"],

@app.get('/')
def to_homepage():

    prompts = silly_story.prompts

    return render_template(
        "questions.html",
        prompts = prompts
    )

@app.get('/results')
def to_results():
    print(request.args)
    text = silly_story.get_result_text(request.args)

    return render_template(
        "results.html",
        text = text
    )
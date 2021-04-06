from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pandaseatbamboo'
debug = DebugToolbarExtension(app)

@app.route('/madlibs_form')
def madlibs_form():
    prompts = story.prompts
    return render_template("madlibs_form.html", prompts =prompts)

@app.route('/story')
def finished_madlibs_story():
    text = story.generate(request.args)
    return render_template('story.html', text=text)
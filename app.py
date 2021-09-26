from flask import Flask, request, render_template
from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)

PROMPTS = stories.story.prompts


@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html', prompts=PROMPTS)


@app.route('/story')
def generate_story():
    """Show the story created based on the input for prompts on the home page"""
    answers = dict(request.args)
    generated_story = stories.story.generate(answers)
    return render_template("story.html", story=generated_story)

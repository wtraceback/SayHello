from app import app
from flask import render_template
from app.forms import HelloWorldForm

@app.route('/')
def index():
    title = 'Hello World'
    form = HelloWorldForm()
    return render_template('index.html', title=title, form=form)

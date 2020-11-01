from app import app
from flask import render_template

@app.route('/')
def index():
    title = 'Hello World'
    return render_template('index.html', title=title)
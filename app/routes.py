from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import HelloWorldForm

@app.route('/', methods=['GET', 'POST'])
def index():
    title = 'Hello World'
    form = HelloWorldForm()
    if form.validate_on_submit():
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', title=title, form=form)

from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import HelloWorldForm
from app.models import Message

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloWorldForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.message.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)

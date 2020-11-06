from app import app, db
from flask import render_template, flash, redirect, url_for, request
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

    page = request.args.get('page', 1, type=int)
    pagination = Message.query.order_by(Message.timestamp.desc()).paginate(page, app.config['MESSAGES_PER_PAGE'], False)
    messages = pagination.items
    return render_template('index.html', form=form, pagination=pagination, messages=messages)

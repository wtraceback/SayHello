from flask import render_template
from .. import db
from . import main


@main.app_errorhandler(400)
def bad_request(e):
    return render_template('errors/400.html'), 400


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('errors/500.html'), 500

import os
import click
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
moment = Moment()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    register_commands(app)

    return app


def register_commands(app):
    @app.cli.command()
    @click.option('--messages', default=100, help='Quantity of messages, default is 100.')
    def forge(messages):
        from app.fakes import fake_messages

        db.drop_all()
        db.create_all()

        click.echo('Generating {} messages...'.format(messages))
        fake_messages(messages)

from faker import Faker
from app import app, db
from app.models import Message
import click


@app.cli.command()
@click.option('--messages', default=100, help='Quantity of messages, default is 100.')
def forge(messages):
    db.drop_all()
    db.create_all()

    click.echo('Generating {} messages...'.format(messages))
    fake_messages(messages)


def fake_messages(count):
    fake = Faker()

    for i in range(count):
        message = Message(
            name = fake.name(),
            body = fake.sentence(),
            timestamp = fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()

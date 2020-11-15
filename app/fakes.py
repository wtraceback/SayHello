from faker import Faker
from app import db
from app.models import Message
import click


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

import os
import sys


WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

basedir = os.path.abspath(os.path.dirname(__file__))
app_db = prefix + os.path.join(basedir, 'app.db')


class Config():
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', app_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MESSAGES_PER_PAGE = 10

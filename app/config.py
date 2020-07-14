"""Flask config."""
from os import environ, path
from flask.cli import load_dotenv

load_dotenv('.env')

DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')
MYSQL_DATABASE_USER = environ.get('MYSQL_DATABASE_USER')
MYSQL_DATABASE_PASSWORD = environ.get('MYSQL_DATABASE_PASSWORD')
MYSQL_DATABASE_DB = environ.get('MYSQL_DATABASE_DB')
MYSQL_DATABASE_HOST = environ.get('MYSQL_DATABASE_HOST')

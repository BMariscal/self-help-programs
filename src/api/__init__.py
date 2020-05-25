import os
import logging

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask


# Defines the format of the logging to include the time and to use the INFO logging level or worse.
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)


POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB =  os.environ.get("POSTGRES_DB")

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{str(POSTGRES_PORT)}/{POSTGRES_DB}'


db = create_engine(DATABASE_CONNECTION_URI, convert_unicode=True)


Base = declarative_base()
Base.metadata.bind = db
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=db))

Base.query = db_session.query_property()



def create_app():
    """
    Flask application factory that creates app instances.
    Every time this function is called, a new application instance is created. The reason
    why an application factory is needed is because we need to use different configurations
    for running our tests.
    :return Flask object: Returns a Flask application instance
    """

    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    # Blueprints are used for scalability. If you want to read more about it, visit:
    # http://flask.pocoo.org/docs/0.12/blueprints/
    from .controllers.routes import website_blueprint
    app.register_blueprint(website_blueprint)

    return app
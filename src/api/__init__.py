import logging
import os
import random

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)

POSTGRES_CONNECTION_URI = os.getenv('DATABASE_URL')

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{POSTGRES_CONNECTION_URI}'

db = create_engine(DATABASE_CONNECTION_URI, convert_unicode=True)

Base = declarative_base()
Base.metadata.bind = db
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=db))

Base.query = db_session.query_property()


def seed_db():
    """
    Seeds tables:
    program(SQLAlchemy Model): Program table object
    section(SQLAlchemy Model): Section table object
    activity(SQLAlchemy Model): QuestionActivity table object
    option(SQLAlchemy Model): QuestionActivityOption table object
    text_activity(SQLAlchemy Model): TextActivity table object

    Returns:
    """
    from .models.db_models import text_activity
    from .models.db_models import section
    from .models.db_models import question_activity_option
    from .models.db_models import question_activity
    from .models.db_models import program
    from .controllers.routes import graphql_blueprint

    PROGRAM_TO_SECTIONS_COUNT = {
        "Leadership Development Program": 10,
        "Cognitive Behavioral Therapy": 8,
        "New Parenting": 4,
        "Mindful Communication": 4,
    }

    program.Program.seed()
    program_entities = program.Program.query.all()
    logger.info("SEEDING DB")
    for entity in program_entities:
        for i in range(PROGRAM_TO_SECTIONS_COUNT[entity.name]):
            section_entity = section.Section.seed(entity, i)
            for j in range(random.randint(2, 5)):
                if j % 2 == 0:
                    question_activity_entity = question_activity.QuestionActivity.seed(
                        section_entity)
                    question_activity_option.QuestionActivityOption.seed(
                        question_activity_entity)
                else:
                    text_activity.TextActivity.seed(section_entity)
    logger.info("COMPLETED SEEDING DB")
    return program_entities


def create_app():
    """
    Flask application factory creates a new application instance.

    Returns:
        Flask object: Returns a Flask application instance
    """

    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # Creates all the models specified in api/models
    from .models.db_models import text_activity
    from .models.db_models import section
    from .models.db_models import question_activity_option
    from .models.db_models import question_activity
    from .models.db_models import program
    from .controllers.routes import graphql_blueprint

    Base.metadata.create_all(db)

    # register graphql route endpoint
    app.register_blueprint(graphql_blueprint)
    return app

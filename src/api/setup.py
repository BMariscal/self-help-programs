import asyncio
import random
import logging
import sys

from .db.database import Base, db
from .db.models import program, question_activity, question_activity_option, section, text_activity

PROGRAM_TO_SECTIONS_COUNT = {
    "Leadership Development Program": 10,
    "Cognitive Behavioral Therapy": 8,
    "New Parenting": 4,
    "Mindful Communication": 4,
}

# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def init_db():
    Base.metadata.create_all(db)

    log.info("CREATING AND SEEDING DB")

    program.Program.seed()
    program_entities = program.Program.query.all()

    for entity in program_entities:
        for i in range(PROGRAM_TO_SECTIONS_COUNT[entity.name]):
            section_entity = section.Section.seed(entity, i)
            for j in range(random.randint(5, 10)):
                if j % 2 == 0:
                    question_activity_entity = question_activity.QuestionActivity.seed(section_entity)
                    question_activity_option.QuestionActivityOption.seed(
                        question_activity_entity)
                else:
                    text_activity.TextActivity.seed(section_entity)
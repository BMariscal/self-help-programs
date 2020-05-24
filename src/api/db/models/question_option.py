from faker import Faker

from ..database import Base, db_session
from sqlalchemy import ARRAY, Column, DateTime, Enum, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship


class QuestionOption(Base):
    __tablename__ = 'questionoption'
    id = Column(Integer, primary_key=True)
    question_option_content = Column(String)
    question_activity_id = Column(Integer, ForeignKey('questionactivities.id'))

    @classmethod
    def seed(cls, question_activity):
        fake = Faker()
        question_option = QuestionOption(
            question_option_content=fake.text(),
            question_activity_id=question_activity.id,
        )
        question_option.save()
        return question_option

    def save(self):
        db_session.add(self)
        db_session.commit()
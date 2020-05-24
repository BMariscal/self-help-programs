from faker import Faker
from sqlalchemy import Column, ForeignKey, Integer, String

from ..database import Base, db_session


class QuestionActivityOption(Base):
    __tablename__ = 'questionactivityoptions'
    id = Column(Integer, primary_key=True)
    question_option_content = Column(String)
    question_activity_id = Column(Integer, ForeignKey('questionactivities.id'))

    @classmethod
    def seed(cls, question_activity):
        fake = Faker()
        question_option = QuestionActivityOption(
            question_option_content=fake.text(),
            question_activity_id=question_activity.id,
        )
        question_option.save()
        return question_option

    def save(self):
        db_session.add(self)
        db_session.commit()

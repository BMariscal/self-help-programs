from faker import Faker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base, db_session


class QuestionActivity(Base):
    __tablename__ = 'questionactivities'
    id = Column(Integer, primary_key=True)
    question_activity_content = Column(String)
    question_options = relationship('QuestionActivityOption', backref='questionactivity')

    section_id = Column(Integer, ForeignKey('sections.id'))

    @classmethod
    def seed(cls, section):
        fake = Faker()
        question_activity = QuestionActivity(
            question_activity_content=fake.text(),
            section_id=section.id,
        )
        question_activity.save()
        return question_activity

    def save(self):
        db_session.add(self)
        db_session.commit()

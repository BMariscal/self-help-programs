from api import Base, db_session
from faker import Faker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class QuestionActivity(Base):
    __tablename__ = "questionactivities"
    id = Column(Integer, primary_key=True)
    question_activity_content = Column(
        String, comment="QuestionActivity Content.")
    question_options = relationship(
        "QuestionActivityOption", backref="questionactivity")
    section_id = Column(Integer, ForeignKey("sections.id"),
                        comment="Section-ID QuestionActivity Belongs To.")

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

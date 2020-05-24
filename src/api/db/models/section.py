from faker import Faker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base, db_session


class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    order_index = Column(Integer)
    overview_image = Column(String)
    program_id = Column(Integer, ForeignKey('programs.id'))

    question_activities = relationship('QuestionActivity', backref="section")
    text_activities = relationship('TextActivity', backref="section")

    @classmethod
    def seed(cls, program, index):
        fake = Faker()
        section = Section(
            name=fake.text(),
            description=fake.text(),
            order_index=index,
            overview_image="https://fakeimg.pl/350x200/ff0000/000",
            program_id=program.id,
        )
        section.save()
        return section

    def save(self):
        db_session.add(self)
        db_session.commit()

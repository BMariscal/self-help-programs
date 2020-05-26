from faker import Faker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ... import Base, db_session


class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True)
    name = Column(String, comment="Name of Section.")
    description = Column(String(500), comment="Section Description.")
    order_index = Column(Integer, comment="Section Order Index.")
    overview_image = Column(String, comment="Section Overview Image.")
    program_id = Column(Integer, ForeignKey("programs.id"), comment="Program ID Section Belongs To.",)

    question_activities = relationship("QuestionActivity", backref="section")
    text_activities = relationship("TextActivity", backref="section")

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

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api import Base, db_session


class Program(Base):
    __tablename__ = 'programs'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    description = Column(String(500))
    sections = relationship('Section', backref='program')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Name Object %r>' % self.id

    @classmethod
    def seed(cls):
        leadership_program = Program(
            name="Leadership Development Program",
            description="Develop leadership skills.",
        )
        leadership_program.save()

        cbt_program = Program(
            name="Cognitive Behavioral Therapy",
            description="Psycho-social intervention that aims to improve mental health.",
        )
        cbt_program.save()

        new_parenting_program = Program(
            name="New Parenting",
            description="Feel more connected with your child and build confidence around your parenting decisions.",
        )
        new_parenting_program.save()

        mindful_communication = Program(
            name="Mindful Communication",
            description="Apply principles of mindfulness to the way you correspond with others.",
        )
        mindful_communication.save()

    def save(self):
        db_session.add(self)
        db_session.commit()
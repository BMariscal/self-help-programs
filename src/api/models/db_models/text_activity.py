from faker import Faker
from sqlalchemy import Column, ForeignKey, Integer, String

from ... import Base, db_session


class TextActivity(Base):
    __tablename__ = "textactivities"
    id = Column(Integer, primary_key=True)
    text_activity_content = Column(String, comment="TextActivity Content.")
    section_id = Column(Integer, ForeignKey("sections.id"),
                        comment="Section-ID TextActivity Belongs To.")

    @classmethod
    def seed(cls, section):
        fake = Faker()
        text_activity = TextActivity(
            text_activity_content=fake.text(),
            section_id=section.id,
        )
        text_activity.save()
        return text_activity

    def save(self):
        db_session.add(self)
        db_session.commit()

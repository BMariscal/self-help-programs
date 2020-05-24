from ..database import Base, db_session
from sqlalchemy import Column, Enum, Integer, String
from .enums import QuestionDifficulty

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_title = Column(String)
    question_title_slug = Column(String)
    question_difficulty = Column(Enum(QuestionDifficulty, name='question_difficulty'))

    @classmethod
    def seed(cls):
        question1 = Question(question_title="Two Sum", question_title_slug="two-sum", question_difficulty="Easy")
        question1.save()

        question2 = Question(question_title="Add Two Numbers", question_title_slug="add-two-numbers",
                             question_difficulty="Medium")
        question2.save()

        question3 = Question(question_title="Longest Substring Without Repeating Characters",
                             question_title_slug="longest-substring-without-repeating-characters",
                             question_difficulty="Medium")
        question3.save()

    def save(self):
        db_session.add(self)
        db_session.commit()



from ..database import Base, db_session
from sqlalchemy import Column, Enum, Integer, ForeignKey
from .enums import SubscriptionDifficulty

class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True)
    difficulty_level = Column(Enum(SubscriptionDifficulty))
    account_id = Column(Integer, ForeignKey('accounts.id'))

    @classmethod
    def seed(cls):
        subscription = Subscription(
            difficulty_level="Easy",
        )
        subscription.save()

        subscription = Subscription(
            difficulty_level="Medium",
        )
        subscription.save()


        subscription = Subscription(
            difficulty_level="Hard",
        )
        subscription.save()

    def save(self):
        db_session.add(self)
        db_session.commit()
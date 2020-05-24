from ..database import Base, db_session
from sqlalchemy import ARRAY, Column, DateTime, Enum, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    # Using default=func.now() to set the default creation time
    created = Column(DateTime, default=func.now())
    timezone = Column(String, default='UTC')
    subscriptions = relationship('Subscription', backref='account')
    problems_sent = Column(ARRAY(Integer), nullable=True)
    problems_completed = Column(ARRAY(Integer), nullable=True)

    @classmethod
    def seed(cls, sub):
        account1 = Account(email="briceidamcamargo@gmail.com", timezone="US/Pacific", subscriptions=[sub],
                           problems_sent=[], problems_completed=[])
        account1.save()

        account2 = Account(email="briceidam@gmail.com", timezone="US/Pacific", subscriptions=[sub],
                           problems_sent=[], problems_completed=[])
        account2.save()

        account3 = Account(email="brico@gmail.com", timezone="US/Pacific", subscriptions=[sub],
                           problems_sent=[], problems_completed=[])
        account3.save()

    def save(self):
        db_session.add(self)
        db_session.commit()
import logging
import sys

from .db.database import Base, db
from .db.models import subscription, account, question


# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def init_db():
    log.info('Creating and Seeding Tables')
    Base.metadata.create_all(db)

    subscription.Subscription.seed()
    subscriptions = subscription.Subscription.query.all()

    for sub in subscriptions:
        account.Account.seed(sub)

    question.Question.seed()

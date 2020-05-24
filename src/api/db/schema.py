from .models import subscription
from .models import question
from .models import account

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class SubscriptionObject(SQLAlchemyObjectType):
    class Meta:
        model = subscription.Subscription
        interfaces = (relay.Node, )


class QuestionObject(SQLAlchemyObjectType):
    class Meta:
        model = question.Question
        interfaces = (relay.Node, )


class AccountObject(SQLAlchemyObjectType):
    class Meta:
        model = account.Account
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allow only single column sorting
    all_accounts = SQLAlchemyConnectionField(AccountObject)
    # Allows sorting over multiple columns, by default over the primary key
    all_questions = SQLAlchemyConnectionField(QuestionObject)
    # Disable sorting over this field
    all_subscriptions = SQLAlchemyConnectionField(SubscriptionObject)


schema = graphene.Schema(query=Query)
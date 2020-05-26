import graphene
from graphene import relay, Int
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from .models.db_models import program, question_activity, question_activity_option, section, text_activity


class CountableConnection(relay.Connection):
    class Meta:
        abstract = True

    total_count = Int()

    @staticmethod
    def resolve_total_count(root, info):
        return root.length


class ProgramObject(SQLAlchemyObjectType):
    class Meta:
        model = program.Program
        interfaces = (relay.Node,)
        connection_class = CountableConnection
        filter_fields = {
            'name': ["exact", "icontains", "istartswith"],
        }


class SectionObject(SQLAlchemyObjectType):
    class Meta:
        model = section.Section
        interfaces = (relay.Node,)
        connection_class = CountableConnection


class QuestionActivityObject(SQLAlchemyObjectType):
    class Meta:
        model = question_activity.QuestionActivity
        interfaces = (relay.Node,)
        connection_class = CountableConnection


class TextActivityObject(SQLAlchemyObjectType):
    class Meta:
        model = text_activity.TextActivity
        interfaces = (relay.Node,)
        text_activity_id = graphene.NonNull(graphene.Int)
        connection_class = CountableConnection


class QuestionActivityOptionObject(SQLAlchemyObjectType):
    class Meta:
        model = question_activity_option.QuestionActivityOption
        interfaces = (relay.Node,)
        appears_in = graphene.NonNull(graphene.Int)
        connection_class = CountableConnection


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    all_text_activities = SQLAlchemyConnectionField(TextActivityObject)
    all_programs = SQLAlchemyConnectionField(ProgramObject)
    all_question_activities = SQLAlchemyConnectionField(QuestionActivityObject)
    all_question_options = SQLAlchemyConnectionField(QuestionActivityOptionObject)
    all_sections = SQLAlchemyConnectionField(SectionObject)

    program = relay.Node.Field(ProgramObject)
    section = relay.Node.Field(SectionObject)
    question_activity = relay.Node.Field(QuestionActivityObject)
    question_option = relay.Node.Field(QuestionActivityOptionObject)
    text_activity = relay.Node.Field(TextActivityObject)


schema = graphene.Schema(query=Query)
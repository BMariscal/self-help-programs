from .db.models import text_activity
from .db.models import program
from .db.models import question_activity
from .db.models import section
from .db.models import question_option

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


#
# class ProgramAttribute:
#     name = graphene.String(description="Name of program.")
#     description = graphene.String(description="Program description.")
#     sections = graphene.String(description="Program sections.")

class ProgramObject(SQLAlchemyObjectType):
    class Meta:
        model = program.Program
        interfaces = (relay.Node,)


# class SectionAttribute:
#     name = graphene.String(description="Name of Section")
#     description = graphene.String(description="Sectiondescription.")
#     ordered_index = graphene.String(description="Index of section.")
#     overview_image =
#     program_id =
#     activity_id


class SectionObject(SQLAlchemyObjectType):
    class Meta:
        model = section.Section
        interfaces = (relay.Node,)


class QuestionActivityObject(SQLAlchemyObjectType):
    class Meta:
        model = question_activity.QuestionActivity
        interfaces = (relay.Node,)



class TextActivityObject(SQLAlchemyObjectType):
    class Meta:
        model = text_activity.TextActivity
        interfaces = (relay.Node,)
        text_activity_id = graphene.NonNull(graphene.Int)


class QuestionOptionObject(SQLAlchemyObjectType):
    class Meta:
        model = question_option.QuestionOption
        interfaces = (relay.Node,)
        appears_in = graphene.NonNull(graphene.Int)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_text_activities = SQLAlchemyConnectionField(TextActivityObject)
    all_programs = SQLAlchemyConnectionField(ProgramObject)
    all_question_activities = SQLAlchemyConnectionField(QuestionActivityObject)
    all_question_options = SQLAlchemyConnectionField(QuestionOptionObject)
    all_sections = SQLAlchemyConnectionField(SectionObject)

    program = graphene.relay.Node.Field(ProgramObject)
    section = graphene.relay.Node.Field(SectionObject)
    question_activity = graphene.relay.Node.Field(QuestionActivityObject)
    question_option = graphene.relay.Node.Field(QuestionOptionObject)
    text_activity = graphene.relay.Node.Field(TextActivityObject)


schema = graphene.Schema(query=Query)

"""
Graphql route registered using Blueprint.
"""
from flask import Blueprint, abort
from flask_graphql import GraphQLView

from ..schema import schema
graphql_blueprint = Blueprint('graphql', __name__)


graphql_blueprint.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

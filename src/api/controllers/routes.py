from flask import render_template, Blueprint
from flask_graphql import GraphQLView


website_blueprint = Blueprint('website_blueprint', __name__)


website_blueprint.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()
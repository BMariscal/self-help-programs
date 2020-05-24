#!/usr/bin/env python
from .setup import init_db
from .db.database import db_session
from .db.schema import schema
from flask_graphql import GraphQLView
from flask import Flask, jsonify


app = Flask(__name__)
app.debug = True
app.before_first_request(init_db)

app.add_url_rule(
    "/all", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(threaded=True, debug=True)

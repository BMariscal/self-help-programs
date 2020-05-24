#!/usr/bin/env python
import asyncio
import logging
import sys

from flask import Flask
from flask_graphql import GraphQLView

from .schema import schema
from .db.database import db_session
from .setup import init_db

app = Flask(__name__)
app.debug = True
asyncio.run(init_db())

# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(threaded=True, debug=True)

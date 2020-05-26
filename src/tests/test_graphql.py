import logging
import unittest

from api import create_app, logger, schema
from flask import url_for
from flask_testing import TestCase
from graphene.test import Client

test_app_instance = create_app()


class TestGraphqlEndpoint(TestCase):
    """
    Test Graphql endpoint.
    """

    def create_app(self):

        # Set application confirguration to 'TestingConfig' to use db_test
        test_app_instance.config.from_object('config.TestingConfig')

        logger.setLevel(logging.ERROR)

        return test_app_instance

    def test_graphiql_is_enabled(self):
        with self.client:
            response = self.client.get(url_for("graphql.graphql", externals=False), headers={"Accept": "text/html"})
        assert response.status_code == 200

    def test_graphql_page__success(self):
        with self.client:
            response = self.client.get(url_for("graphql.graphql", query="{test}"), headers={"Accept": "text/html"})
            self.assertEqual(response.status_code, 200)

    def test_graphql_page__failure(self):
        with self.client:
            response = self.client.get('/graphql')
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()

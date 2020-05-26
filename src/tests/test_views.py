import logging
import unittest

from api import create_app, logger
from api import schema as Schema
from flask_testing import TestCase
from graphene.test import Client

test_app_instance = create_app()


class TestGraphqlQuery(TestCase):

    def create_app(self):
        """
        Instructs Flask to run these commands when we request this group of tests to be run.
        """

        # Set application confirguration to 'TestingConfig' to use db_test.
        test_app_instance.config.from_object('config.TestingConfig')

        logger.setLevel(logging.ERROR)

        return test_app_instance

    def setUp(self):
        self.client = Client(Schema.schema)

    def test_graphql_programs__successful(self):
        if self.client:
            executed = self.client.execute(
                '''{ allPrograms {
                        edges {
                            node {
                                id
                                name
                                }
                            }
                        }
                    }''')

            assert executed == {'data': {'allPrograms': {
                'edges': [{'node': {'id': 'UHJvZ3JhbU9iamVjdDox', 'name': 'Leadership Development Program'}},
                          {'node': {'id': 'UHJvZ3JhbU9iamVjdDoy', 'name': 'Cognitive Behavioral Therapy'}},
                          {'node': {'id': 'UHJvZ3JhbU9iamVjdDoz', 'name': 'New Parenting'}},
                          {'node': {'id': 'UHJvZ3JhbU9iamVjdDo0', 'name': 'Mindful Communication'}}]}}}

    def test_graphql_one_program__all_sections__successful(self):
        if self.client:
            executed = self.client.execute(
                '''{
            program (id: "UHJvZ3JhbU9iamVjdDox"){
                id
                name
                description
                sections {
                  edges {
                    node {
                      id
                      name
                      description
                      orderIndex
                      overviewImage
                      programId
                     
                }
                    }
                  }
                }
              }     
                ''')
            assert executed["data"]["program"]["id"] == "UHJvZ3JhbU9iamVjdDox"
            assert executed["data"]["program"]["sections"]["edges"][0]["node"]["orderIndex"] == 0
            assert executed["data"]["program"]["sections"]["edges"][1]["node"]["orderIndex"] == 1

    def test_graphql_one_program__one_section__successful(self):
        if self.client:
            executed = self.client.execute(
                '''{
                
                  program (id: "UHJvZ3JhbU9iamVjdDox"){
                    id
                    name
                    description
                    sections (first:1) {
                      edges {
                        node {
                          id
                          name
                          description
                          orderIndex
                          overviewImage
                          programId
                              
                             }
                        }
                      }
                    }
                  }
                   
                ''')
            assert len(executed["data"]["program"]["sections"]["edges"]) == 1

    def test_graphql_query_with_cursor__successful(self):
        if self.client:
            executed = self.client.execute(
                '''
                    {
                      allPrograms {
                        edges {
                          node {
                            id
                            name
                            sections(first: 2) {
                              totalCount
                              edges {
                                node {
                                  id
                                  name
                                  description
                                }
                                cursor
                              }
                              pageInfo {
                                endCursor
                                hasNextPage
                              }
                            }
                          }
                        }
                      }
                    }


                ''')
            assert type(executed["data"]["allPrograms"]["edges"][0]["node"]["sections"]["edges"][0]["cursor"]) == str

    def test_graphql_query_program_sectionsactivties__success(self):
        if self.client:
            executed = self.client.execute(
                '''
        {
          program(id: "UHJvZ3JhbU9iamVjdDox") {
            id
            name
            description
            sections {
              edges {
                node {
                  id
                  name
                  description
                  orderIndex
                  overviewImage
                  programId
                  questionActivities {
                    edges {
                      node {
                        id
                        questionActivityContent
                        sectionId
                        questionOptions {
                          edges {
                            node {
                              questionOptionContent
                              questionActivityId
                            }
                          }
                        }
                      }
                    }
                  }
                  textActivities {
                    edges {
                      node {
                        id
                        textActivityContent
                        sectionId
                      }
                    }
                  }
                }
              }
            }
          }
        }
                ''')

            assert executed != None


if __name__ == '__main__':
    unittest.main()

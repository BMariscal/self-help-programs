# from graphene.test import Client
# from src.api.schema import schema
#
# def test_hey():
#     client = Client(schema)
#     executed = client.execute('''{ hey }''', context={'user': 'Peter'})
#     assert executed == {
#         'data': {
#             'hey': 'hello Peter!'
#         }
#     }
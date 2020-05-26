"""
Entry point of the Flask application.
"""
import asyncio
import unittest
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from api import create_app, seed_db, db_session, Base
from flask_script import Manager

# Initialize Flask app.
app = create_app()

# Initialize the Manager object to run terminal commands on the application.
manager = Manager(app)

@manager.command
def create_fixtures():
    """Seed Postgres DB."""
    seed_db()

@manager.command
def test():
    """
    Runs tests.

    Enter 'docker-compose run --rm api python manage.py test' to run all the tests in the
    'tests' directory.

    Returns:
         int: 0 if all tests pass
         int: 1 if otherwise
    """


    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


if __name__ == '__main__':
    manager.run()
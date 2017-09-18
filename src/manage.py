import unittest

from apps import app, db
from flask_script import Manager


app.config.from_object('config.TestConfig')
manager = Manager(app)

@manager.command
def test():
    """Runs the unit tests without coverage."""
    #print('testing test')
    tests = unittest.TestLoader().discover('apps.video.tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()

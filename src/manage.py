import unittest

from apps import app, db
from flask_script import Manager


app.config.from_object('config.TestConfig')
manager = Manager(app)


@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('apps.video.tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def run():
    db.create_all()
    app.config.from_object('config.Config')
    app.run(host=app.config['SERVER_IP'], port=app.config['PORT'])
    # app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    manager.run()

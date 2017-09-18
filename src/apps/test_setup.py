import os
from flask.ext.testing import TestCase
import unittest
from apps import db, app
from flask import request


class ArkTestCase(unittest.TestCase):

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        self.db = db
        app.config.from_object('config.TestConfig')
        self.app = app.test_client()

        with app.app_context():
            self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

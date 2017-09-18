import unittest

from flask import request

from apps.test_setup import ArkTestCase
from apps import app, db
from apps.video.models import Video


class TestVideo(ArkTestCase):

    def setUp(self):
        db.session.add(Video.add_title(self=Video, title='Added test title'))

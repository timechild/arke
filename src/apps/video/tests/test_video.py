import unittest

from apps.test_setup import ArkTestCase
from apps.video.models.video import Video

from flask import request


class FlaskrTestCase(ArkTestCase):
    '''
    def setUp(self):
        db.session.add(Video.add_title(self=Video, title='Added test title'))
    '''

    def test_index(self):
        response = self.app.post('/video', content_type='html/text')
        self.assertEqual(b'<h1>Welcome To APPSssss</h1>', response.data)

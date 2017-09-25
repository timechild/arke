import unittest

from . import VideoTestBase
from apps.video.models.video import Video

from flask import request, json


class FlaskrTestCase(VideoTestBase):

    def test_index(self):
        response = self.app.post('/video', content_type='html/text')
        self.assertEqual(b'<h1>Welcome To Video Page</h1>', response.data)

    def test_database_entry(self):

        response = self.app.post('/video-database',
                                 content_type='application/json',
                                 data=json.dumps(dict(
                                     title='CNN Video',
                                     description='Video description',
                                     url='cnn.com',
                                     source='CNN',
                                     iframe='<iframe>cnn.com/video</iframe>')))

        video = Video.query.filter_by(title='CNN Video').first()
        self.assertEqual(video.title, 'CNN Video')
        self.assertEqual(response.status_code, 200)

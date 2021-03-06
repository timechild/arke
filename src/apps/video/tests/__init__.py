import unittest

from apps import db, app
from apps.video.models.video import Video


class VideoTestBase(unittest.TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        self.app = self.create_app()
        self.app = app.test_client()
        self.db = db
        self.db.create_all()

        Video.add_video(self=Video,
                        title='CNN Title Video',
                        description='Video-test description',
                        url='cnn.com',
                        source='CNN',
                        iframe='<iframe>cnn.com/video</iframe>')

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

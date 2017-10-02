from flask import json
from .models.video import Video


class VideoSerializer(object):
    def serialze_video(self):
        data = dict(id=self.id,
                    title=self.title,
                    description=self.description,
                    url=self.url,
                    source=self.source,
                    iframe=self.iframe)

        return json.dumps(data)

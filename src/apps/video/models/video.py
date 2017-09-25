from apps import db


class Video(db.Model):
    id = db.Column('video_id', db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(1500))
    url = db.Column(db.String(500))
    iframe = db.Column(db.String(1000))
    source = db.Column(db.String(250))

    def add_video(self, title, description, url, source, **kwargs):
        video = Video()
        video.title = title
        video.description = description
        video.url = url
        video.source = source
        video.iframe = kwargs.get('iframe', None)
        db.session.add(video)
        db.session.commit()

    def update_video(self, video_id, **kwargs):
        """update the video"""
        video = Video.query.filter_by(id=video_id).first()
        video.title = kwargs.get('title', video.title)
        video.description = kwargs.get('description', video.description)
        video.url = kwargs.get('url', video.url)
        video.source = kwargs.get('source', video.source)
        video.iframe = kwargs.get('iframe', video.iframe)
        db.session.commit()

from apps import db


class Video(db.Model):
    id = db.Column('video_id', db.Integer, primary_key=True)
    title = db.Column(db.String(250))

    def add_title(self, title):
        video = Video()
        video.title = title
        db.session.add(video)
        db.session.commit()

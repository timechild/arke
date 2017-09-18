from flask import flash, redirect, render_template, request, \
    url_for, Blueprint
from apps.video.models.video import Video

video_blueprint = Blueprint(
    'video', __name__
)


@video_blueprint.route('/video', methods=['GET', 'POST'])
def index():
    Video.add_title(self=Video, title='Added test title')
    return '<h1>Welcome To APPSssss</h1>'

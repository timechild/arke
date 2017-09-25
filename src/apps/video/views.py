from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, json, Response
from apps.video.models.video import Video

video_blueprint = Blueprint(
    'video', __name__
)


@video_blueprint.route('/video', methods=['GET', 'POST'])
def index():
    return '<h1>Welcome To Video Page</h1>'


@video_blueprint.route('/video-to-database', methods=['GET', 'POST'])
def add_video_to_database():
    content = request.get_json(silent=True)
    Video.add_title(self=Video,
                    title=content['title'],
                    description=content['description'],
                    url=content['url'],
                    source=content['source'],
                    iframe=content['iframe'])

    return Response({'success': True}, status=200, mimetype='application/json')

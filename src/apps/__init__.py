import os
from apps.video.views import video_blueprint
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

# register our blueprints
app.register_blueprint(video_blueprint)

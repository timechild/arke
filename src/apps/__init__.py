from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

# assign blueprints
from apps.video.views import video_blueprint
app.register_blueprint(video_blueprint)

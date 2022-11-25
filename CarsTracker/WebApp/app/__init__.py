from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.views import IndexView
from app.config import Config


app_flask = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

db.init_app(app=app_flask)
migrate.init_app(app=app_flask, db=db)

app_flask.config.from_object(Config)
app_flask.add_url_rule('/index', view_func=IndexView.as_view('index'))

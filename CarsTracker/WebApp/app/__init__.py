from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from app.views import IndexView, RegisterView, LoginView
from app.config import Config


app_flask = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt(app_flask)

db.init_app(app=app_flask)
migrate.init_app(app=app_flask, db=db)

app_flask.config.from_object(Config)
app_flask.secret_key = Config.SECRET_KEY
app_flask.add_url_rule('/index', view_func=IndexView.as_view('index'))
app_flask.add_url_rule('/register', view_func=RegisterView.as_view('register'))
app_flask.add_url_rule('/login', view_func=LoginView.as_view('login'))

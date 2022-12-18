from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from app.config import Config

app_flask = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt(app_flask)

db.init_app(app=app_flask)
migrate.init_app(app=app_flask, db=db)

from app.views import IndexView, RegisterView, LoginView, LogoutView, HomeView

app_flask.config.from_object(Config)
app_flask.secret_key = Config.SECRET_KEY
app_flask.add_url_rule('/', view_func=IndexView.as_view('index'), methods=["GET"])
app_flask.add_url_rule('/home', view_func=HomeView.as_view('home'), methods=["GET"])
app_flask.add_url_rule('/register', view_func=RegisterView.as_view('register'), methods=["GET", "POST"])
app_flask.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=["GET", "POST"])
app_flask.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))

from app.models import Users

login_manager = LoginManager()
login_manager.login_view = 'views.login'
login_manager.init_app(app_flask)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
from flask import render_template, url_for, redirect, request, flash
from flask.views import View, MethodView

from app.forms import RegisterForm
from app import db
from .models import Users
from .states import UserStates


class IndexView(View):

    def __init__(self):
        self.welcome_text = "Hello!"

    def dispatch_request(self):
        return render_template("base.html")


class RegisterView(MethodView):

    def __register_to_db(self, register_form):
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data

        user = Users.query.filter_by(email=email | username=username).first()
        if user is not None:
            return UserStates.ALREADY_EXISTING   
            
        new_user = Users(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return UserStates.CREATED

    def get(self):
        register_form = RegisterForm(request.method)
        return render_template("register.html", register_form=register_form)

    def post(self):
        register_form = RegisterForm(request.method)
        if register_form.validate():
            state = self.__register_to_db(register_form=register_form)

            if state == UserStates.ALREADY_EXISTING:
                flash("User with such email or username already exists!")
                return render_template('register.html', register_form=RegisterForm())
            elif state == UserStates.CREATED:
                flash("User account successfully created!")
                redirect(url_for('login'))

        flash('Form data is not valid!')
        return render_template('register.html', register_form=RegisterForm())    


class LoginView(MethodView):

    def __login_user(self):
        pass
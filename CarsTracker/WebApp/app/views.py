from flask import render_template, url_for, redirect, request, flash
from flask.views import View, MethodView

from .forms import RegisterForm
from .models import Users
from .states import UserStates
from app import db


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

        existing_user_email = Users.query.filter_by(email=email).first()
        existing_user_name = Users.query.filter_by(username=username).first()

        if existing_user_email or existing_user_name is not None:
            return UserStates.ALREADY_EXISTING   
            
        new_user = Users(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return UserStates.CREATED

    def get(self):
        register_form = RegisterForm(request.form)
        return render_template("register.html", register_form=register_form)

    def post(self):
        register_form = RegisterForm(request.form)
        if register_form.validate():
            state = self.__register_to_db(register_form=register_form)

            if state == UserStates.ALREADY_EXISTING:
                flash("User with such email or username already exists!", category='error')
                return render_template('register.html', register_form=RegisterForm())
            elif state == UserStates.CREATED:
                flash("User account successfully created!", category='success')
                redirect(url_for('login'))
        else:
            flash('Form data is not valid!', category='error')

        return render_template('register.html', register_form=RegisterForm())    


class LoginView(MethodView):

    def __login_user(self):
        pass
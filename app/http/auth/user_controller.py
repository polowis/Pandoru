

from app.http.controller import Controller
from app import db
from app.http.auth.form import LoginForm, RegisterForm
from app.model.user import User
from flask_login import current_user, login_user, logout_user
from flask import request, session
from werkzeug.urls import url_parse
from app.framework.requests import requests





class User_Controller(Controller):

    def login(self):
        if current_user.is_authenticated:
            return self.redirect_to('/home')
        form = LoginForm()
        username = requests('username')
        password = requests('password')
        if username == '' or password == '':
            self.flash_message('Field cannot be empty')
            self.redirect_to('/')
        else:
            user = User.query.filter_by(email=username).first()
            if user is None and not user.check_password(password):
                self.flash_message('Invalid username or password')
                return self.redirect_to('/')
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = '/home'
        return self.redirect_to(next_page)
    
    def register(self):
        if current_user.is_authenticated:
            return self.redirect_to('/home')
        form = RegisterForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            self.flash_message('Congratulations, you are now a registered user!')
            return self.redirect_to('/home')
        return self.view('register', title='Register', form=form)

    def logout(self):
        logout_user()
        return self.redirect_to('/')

UserController = User_Controller()
from app.http.controller import Controller
from app.http.auth.form import LoginForm
from flask_login import login_required, current_user
from flask import request, session

class Home_Controller(Controller):
    def home(self):
        print(session.get('user'))
        return self.view('home')

    def index(self):
        
        if current_user.is_authenticated:
            return self.redirect_to('/home')
        form = LoginForm()
        return self.view('index', title='Sign In', form=form)

HomeController = Home_Controller()
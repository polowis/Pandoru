from flask import render_template, flash, redirect
from app import app, login
from app.http.auth.form import LoginForm
from app.http.auth.user_controller import UserController
from app.http.home_controller import Home_Controller
from flask_login import login_required, current_user
from app.framework.routes import route
from app.http.home_controller import HomeController

@login.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')

    if token is not None:
        username,password = token.split(":") # naive token
        user_entry = User.get(username)
        if (user_entry is not None):
            user = User(user_entry[0],user_entry[1])
            if (user.password == password):
                return user
    return None



route.get('/', HomeController.index)
route.post('/login', UserController.login)


@app.route('/home', methods=['GET'])
@login_required
def home():
    return Home_Controller().home()

@app.route('/logout', methods=['POST'])
def logout():
    return User_Controller().logout()

@app.route('/register', methods=['POST', 'GET'])
def register():
    return User_Controller().register()
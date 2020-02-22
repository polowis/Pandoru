from flask import render_template, flash, redirect
from app import app, login
from app.http.auth.form import LoginForm
from app.http.auth.user_controller import User_Controller
from app.http.home_controller import Home_Controller
from flask_login import login_required, current_user

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

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect('/home')
    form = LoginForm()
    return render_template('index.html', title='Sign In', form=form)

@app.route('/login', methods=['POST'])
def login():
    return User_Controller().login()

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
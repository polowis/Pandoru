from flask import render_template, flash, redirect
from app import app
from app.http.auth.form import LoginForm
from app.http.auth.user_controller import User_Controller
from flask_login import login_required, logout_user

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    form = LoginForm()
    return render_template('index.html', title='Sign In', form=form)

@app.route('/login', methods=['POST'])
def login():
    return User_Controller().login()

@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html', title="home")

@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect('/')
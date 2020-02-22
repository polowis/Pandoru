from app.http.controller import Controller
from app.http.auth.form import LoginForm
from flask_login import current_user, login_user
from app.model.user import User

class User_Controller(Controller):

    def login(self):
        if current_user.is_authenticated:
            return self.redirect_to('/home')
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return self.redirect_to('/')
        return self.view('index', title='Sign In', form=form)
    



from app.http.controller import Controller
from app.http.auth.form import LoginForm

class Home_Controller(Controller):
    def home(self):
        return self.view('home')
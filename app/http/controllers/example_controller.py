from app import app
from app.framework.controller import Controller, route
from flask_login import login_required

class ExampleController(Controller):

    def construct(cls):
        ExampleController.register(app)

    @route('/test1', methods=["GET"])
    @login_required
    def test(self):
        return self.view('test')


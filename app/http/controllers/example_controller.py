from app import app
from app.framework.controller import Controller, route

class ExampleController(Controller):

    def construct(cls):
        ExampleController.register(app)

    @route('/test1', methods=["GET"])
    def test(self):
        return self.view('test')


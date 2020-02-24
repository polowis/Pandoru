from app.framework.controller import Controller

for classes in Controller.__subclasses__():
    classes().construct()
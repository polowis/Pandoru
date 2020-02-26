from app.framework.controller import Controller
from app.http.exception import view_exception
from app.http import controllers

for classes in Controller.__subclasses__():
    classes().construct()
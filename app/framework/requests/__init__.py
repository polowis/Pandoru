from flask import request

def requests(name):
    return request.form.get(name)
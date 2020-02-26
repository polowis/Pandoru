from flask import request

def requests(name):
    return request.form.get(name)


class Request:
    def register(cls, validation):
        for index, value in validation:
            try:
                result = requests(index)
            except:
                print()

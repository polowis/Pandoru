from flask import request

def requests(name):
    return request.form.get(name)


class Request:
    TYPE = ['integer', 'alpha', 'alphanumeric', 'email']
    def register(cls, validation: list):
        for index, value in validation:
            try:
                result = requests(index)
                self.validate(result, value)
            except:
                print(f'Not found {index}')
        
    def validate(self, index: str, value: str):
        for i in TYPE:
            if value == TYPE:
                return validate_with(index, value)
    
    def validate_with(self, index: str, value: str):
        if value == 'integer':
            return validate_integer(value)
    
    
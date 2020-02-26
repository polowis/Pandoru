class Validator:
    @staticmethod
    def validate_integer(value):
        try:
            result = int(value)

        except ValueError:
            return False
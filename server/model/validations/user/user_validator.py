from cerberus import Validator
from .my_validator import MyValidator


class UserValidator:

    def __init__(self):
        self.v = MyValidator()
        self.schema = {
            'username': {
                "type": "string"
            },
            'password': {
                "type": "string",
                # "check_with": "strong_password"
            },
            'require_all': True
        }

    def is_user_valid(self, user):
        return self.v.validate(user, self.schema)

    def get_errors(self):
        return self.v.errors

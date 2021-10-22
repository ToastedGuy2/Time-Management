from cerberus import Validator
from .my_validator import MyValidator


class UserValidator:

    def __init__(self):
        self.v = MyValidator(require_all=True)
        self.schema = {
            'username': {
                "type": "string",
                'empty': False,
                "check_with": "is_username_already_taken",
            },
            'password': {
                "type": "string",
                'empty': False,
                "check_with": "strong_password",
            },
        }

    def is_user_valid(self, user):
        return self.v.validate(user, self.schema)

    def get_errors(self):
        errors_dict = self.v.errors
        for key in errors_dict:
            error_message = errors_dict[key][0]
            errors_dict[key] = error_message
        return errors_dict

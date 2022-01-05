from .my_validator import MyValidator


class UserValidator:

    def __init__(self):
        self.v = MyValidator(require_all=True)
        self.schema = {
            'username': {
                "type": "string",
                'empty': False,
            },
            'password': {
                "type": "string",
                'empty': False,
                "check_with": "strong_password",
            },
        }

    def is_user_valid(self, user = {}):
        if user is None:
            raise ValueError('Please provide a user dictionary')
        return self.v.validate(user if user else {}, self.schema)

    def get_cleaner_error_messages(self, errors_dict):
        clean_dict = {}
        for key in errors_dict:
            error_message = errors_dict[key][0]
            clean_dict[key] = error_message
        return clean_dict

    def get_errors(self):
        return self.get_cleaner_error_messages(self.v.errors)

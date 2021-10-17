from cerberus import Validator
from .user_validations import UserValidations


class MyValidator(Validator):
    def _check_with_strong_password(self, field, value):
        v = UserValidations()
        if not v.is_password_strong(password=value):
            self._error(
                field, "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_.`")

from cerberus import Validator
from .user_validations import UserValidations
from ....repositories.user_repository import UserRepository


class MyValidator(Validator):
    def __init__(self, *args, **kwargs) -> None:
        super(MyValidator, self).__init__(*args, **kwargs)
        self.v = UserValidations()

    def _check_with_strong_password(self, field, value):
        if not self.v.is_password_strong(password=value):
            self._error(
                field, "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_`")

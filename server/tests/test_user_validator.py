from ..model.validations.user.user_validator import UserValidator


class TestUserValidator:
    def test_password_is_wrong(self):
        uv = UserValidator()
        return uv.is_user_valid({'username': 'pepefrog', 'password': '_Hello_World1'})

    def test_password_is_wrong(self):
        uv = UserValidator()
        if not uv.is_user_valid({'username': 'pepefrog', 'password': 'Hello_World'}):
            assert uv.get_errors()[
                'password'] == 'Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'

    def test_fields_are_required(self):
        uv = UserValidator()
        if not uv.is_user_valid({'username': '', 'password': ''}):
            errors = uv.get_errors()
            assert errors == {}

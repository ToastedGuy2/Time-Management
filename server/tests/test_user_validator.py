from ..utils.validations.user.user_validator import UserValidator


class TestUserValidator:
    def test_fields_are_required(self, mocker):
        uv = UserValidator()
        if not uv.is_user_valid({}):
            errors = uv.get_errors()
            assert errors == {
                'username': 'required field',
                'password': 'required field',
            }

    def test_fields_are_not_empty(self, mocker):
        uv = UserValidator()
        if not uv.is_user_valid({'username': '', 'password': ''}):
            errors = uv.get_errors()
            assert errors == {
                'username': 'empty values not allowed',
                'password': 'empty values not allowed',
            }

    def test_password_is_wrong(self, mocker):
        uv = UserValidator()
        mocker.patch(
            'server.repositories.user_repository.UserRepository.is_there_an_user_with_such_username', return_value=False)

        uv.is_user_valid({'username': 'pepefrog', 'password': 'Hello_World'})
        actual = uv.get_errors()

        assert actual == {
            'password': "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_.`"}

    def test_user_is_invalid(self, mocker):
        uv = UserValidator()
        uv.is_user_valid({'username': '', })
        assert uv.get_errors() == {
            'username': 'empty values not allowed', 'password': 'required field'}
        uv.is_user_valid({'password': '', })
        assert uv.get_errors() == {
            'password': 'empty values not allowed', 'username': 'required field'}
        uv.is_user_valid({'username': 'kkk', 'password': 'kas_as12'})
        assert uv.get_errors() == {
            'password': "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_.`"}

    def test_user_is_valid(self, mocker):
        uv = UserValidator()
        assert uv.is_user_valid(
            {'username': 'pepefrog', 'password': '_Hello_World1'})

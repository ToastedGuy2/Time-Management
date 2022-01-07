from ..utils.validations.user.user_validator import UserValidator
from random_username.generate import generate_username
from password_generator import PasswordGenerator
from pytest import fixture


class TestUserValidator():
    
    @fixture
    def uv(self) -> UserValidator:
        return UserValidator()

    def test_error_messages_are_formatted_well(self,uv:UserValidator):
        input = {
            'username': ['username already exists'],
            'password': ['You got a weak password']
        }
        expected = {
            'username': 'username already exists',
            'password': 'You got a weak password'
        }
        actual = uv.get_cleaner_error_messages(input)
        assert expected == actual

    def test_user_is_valid(self,uv:UserValidator):
        pwg = PasswordGenerator()
        pwg.minlen = 8
        pwg._schars = "@%+\/'!#$^?:.(){[]}~-_`"
        for i in range(1000):
            user = {
                'username': generate_username(1)[0],
                'password': pwg.generate()
            }
            assert uv.is_user_to_create_valid(user) is True

    def test_user_is_not_valid(self,uv:UserValidator):
        pwg = PasswordGenerator()
        pwg.maxlen = 7
        for i in range(1000):
            user = {
                'username': generate_username(5),
                'password': pwg.generate()
            }
            assert uv.is_user_to_create_valid(user) is False

    def test_get_an_empty_error_message_dictionary(self,uv:UserValidator):
        error_message = uv.get_errors()
        assert {} == error_message

    def test_fields_are_required(self,uv:UserValidator):
        user = {}
        uv.is_user_to_create_valid(user)
        actual = uv.get_errors()
        expected = {"username": "required field", "password": "required field"}
        assert expected == actual

    def test_fields_are_not_empty(self,uv:UserValidator):
        user = {'username': '', 'password': ''}
        uv.is_user_to_create_valid(user)
        actual_errors = uv.get_errors()
        expected_errors = {
            'username': 'empty values not allowed',
            'password': 'empty values not allowed',
        }
        assert expected_errors == actual_errors

    def test_password_is_wrong(self,uv:UserValidator):
        uv.is_user_to_create_valid(
            {'username': 'pepefrog', 'password': 'Hello_World'})
        actual_errors = uv.get_errors()
        expected_errors = {
            'password': "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_`"}
        assert expected_errors == actual_errors

    def test_get_error_messages_from_random_inputs(self,uv:UserValidator):
        # 1
        uv.is_user_to_create_valid({'username': '', })
        expected = {
            'username': 'empty values not allowed', 'password': 'required field'
        }
        actual = uv.get_errors()
        assert expected == actual
        # 2
        uv.is_user_to_create_valid({'password': '', })
        expected = {
            'password': 'empty values not allowed', 'username': 'required field'}
        actual = uv.get_errors()
        assert expected == actual
        # 3
        uv.is_user_to_create_valid({'username': 'kkk', 'password': 'kas_as12'})
        expected = {"password":
                    "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_`"
                    }
        actual = uv.get_errors()
        assert expected == actual
    
    def test_is_user_valid_using_an_empty_object(self,uv:UserValidator):
        assert uv.is_user_to_create_valid(None) is False

from ..utils.validations.user.user_validator import UserValidator
import unittest
from random_username.generate import generate_username
from password_generator import PasswordGenerator

from unittest.mock import MagicMock


class TestUserValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.uv = UserValidator()

    def test_error_messages_are_formatted_well(self):
        input = {
            'username': ['username already exists'],
            'password': ['You got a weak password']
        }
        expected = {
            'username': 'username already exists',
            'password': 'You got a weak password'
        }
        actual = self.uv.get_cleaner_error_messages(input)
        self.assertEqual(expected, actual)

    def test_user_is_valid(self):
        pwg = PasswordGenerator()
        pwg.minlen = 8
        pwg._schars = "@%+\/'!#$^?:.(){[]}~-_`"
        for i in range(1000):
            user = {
                'username': generate_username(1)[0],
                'password': pwg.generate()
            }
            self.assertTrue(self.uv.is_user_valid(user))

    def test_user_is_not_valid(self):
        pwg = PasswordGenerator()
        pwg.maxlen = 7
        for i in range(1000):
            user = {
                'username': generate_username(5),
                'password': pwg.generate()
            }
            self.assertFalse(self.uv.is_user_valid(user))

    def test_get_an_empty_error_message_dictionary(self):
        error_message = self.uv.get_errors()
        self.assertEqual({}, error_message)

    def test_fields_are_required(self):
        user = {}
        self.uv.is_user_valid(user)
        actual = self.uv.get_errors()
        expected = {"username": "required field", "password": "required field"}
        self.assertEqual(expected, actual)

    def test_fields_are_not_empty(self):
        user = {'username': '', 'password': ''}
        self.uv.is_user_valid(user)
        actual_errors = self.uv.get_errors()
        expected_errors = {
            'username': 'empty values not allowed',
            'password': 'empty values not allowed',
        }
        self.assertEqual(expected_errors, actual_errors)

    def test_password_is_wrong(self):
        self.uv.is_user_valid(
            {'username': 'pepefrog', 'password': 'Hello_World'})
        actual_errors = self.uv.get_errors()
        expected_errors = {
            'password': "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_`"}
        self.assertEqual(expected_errors, actual_errors)

    def test_get_error_messages_from_random_inputs(self):
        # 1
        self.uv.is_user_valid({'username': '', })
        expected = {
            'username': 'empty values not allowed', 'password': 'required field'
        }
        actual = self.uv.get_errors()
        self.assertEqual(expected, actual)
        # 2
        self.uv.is_user_valid({'password': '', })
        expected = {
            'password': 'empty values not allowed', 'username': 'required field'}
        actual = self.uv.get_errors()
        self.assertEqual(expected, actual)
        # 3
        self.uv.is_user_valid({'username': 'kkk', 'password': 'kas_as12'})
        expected = {"password":
                    "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_`"
                    }
        actual = self.uv.get_errors()
        self.assertEqual(expected, actual)

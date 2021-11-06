from ..repositories.user_repository import UserRepository
from ..models.User import User
import unittest
from unittest.mock import MagicMock


class TestUserRepository(unittest.TestCase):

    def test_user_is_found(self):
        u = UserRepository()
        u.get_by_username = MagicMock(return_value=User())
        actual = u.does_user_exist('hello_world')
        u.get_by_username.assert_called_once_with('hello_world')
        self.assertTrue(actual)

    def test_user_is_not_found(self):
        u = UserRepository()
        u.get_by_username = MagicMock(return_value=None)
        actual = u.does_user_exist('hello_world')
        u.get_by_username.assert_called_once_with('hello_world')
        self.assertFalse(actual)

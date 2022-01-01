from ..repositories.user_repository import UserRepository
from ..models.User import User
from pytest import fixture
from unittest.mock import MagicMock


class TestUserRepository():

    @fixture
    def user(self):
        return UserRepository()
    def test_user_is_found(self,user):
        user.get_by_username = MagicMock(return_value=User())
        actual = user.does_user_exist('hello_world')
        user.get_by_username.assert_called_once_with('hello_world')
        assert actual is True

    def test_user_is_not_found(self,user):
        user.get_by_username = MagicMock(return_value=None)
        actual = user.does_user_exist('hello_world')
        user.get_by_username.assert_called_once_with('hello_world')
        assert actual is False

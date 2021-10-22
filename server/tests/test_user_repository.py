from ..repositories.user_repository import UserRepository
from ..models.User import User
from ..shared.database import db


class TestUserRepository:

    def test_user_is_found(self, mocker):
        mocked_get_by_username = mocker.patch(
            'server.repositories.user_repository.UserRepository.get_by_username', return_value=User())
        u = UserRepository()
        expected = True
        actual = u.is_there_an_user_with_such_username('hello_world')
        assert expected == actual
        u.get_by_username.assert_called_once_with('hello_world')

    def test_user_is_not_found(self, mocker):
        mocker.patch(
            'server.repositories.user_repository.UserRepository.get_by_username', return_value=None)
        u = UserRepository()
        expected = False
        actual = u.is_there_an_user_with_such_username('hello_world')
        assert expected == actual
        u.get_by_username.assert_called_once_with('hello_world')

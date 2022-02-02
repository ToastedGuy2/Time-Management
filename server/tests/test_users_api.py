from flask.testing import FlaskClient
from unittest.mock import MagicMock, patch
from itsdangerous import json
from pytest import fixture
from ..app import app
from ..app import db
from json import loads


class TestUsersApi():
    @fixture
    def client(self):
        with app.test_client() as c:
            app.app_context().push()
            db.drop_all()
            db.create_all()
            yield c

    def test_post_method_with_None_data_so_it_returns_400_bad_request(self, client: FlaskClient):
        # Arrange
        input = None
        # Act
        response = client.post('/api/users', json=input)
        body = loads(response.data.decode('utf-8'))
        # Assert
        assert response.status_code == 400 and body == {
            'message': "Please provide a json object"}

    def test_post_method_with_empty_dict_so_it_returns_400_bad_request(self, client: FlaskClient):
        # Arrange
        input = {}
        # Act
        response = client.post('/api/users', json=input)
        body = loads(response.data.decode('utf-8'))
        # Assert
        assert response.status_code == 400 and body == {'errors': {
            'password': 'required field', 'username': 'required field'}, 'message': 'invalid data'}

    def test_post_method_with_empty_fields_so_it_returns_400_bad_request(self, client: FlaskClient):
        # Arrange
        input = {'password': '', 'username': ''}
        # Act
        response = client.post('/api/users', json=input)
        body = loads(response.data.decode('utf-8'))
        # Assert
        assert response.status_code == 400 and body == {'errors': {
            'password': 'empty values not allowed', 'username': 'empty values not allowed'}, 'message': 'invalid data'}

    def test_post_method_by_trying_to_post_same_input_twice_so_it_must_return_400_bad_request_since_user_is_already_created(self, client: FlaskClient):
        # Arrange
        input = {'password': 'Strong_Password2', 'username': 'test'}
        # Act
        client.post('/api/users', json=input)
        response = client.post('/api/users', json=input)
        # Assert
        assert response.status_code == 400

    def test_post_method_by_including_input_with_an_invalid_password_so_it_returns_400_bad_request(self, client: FlaskClient):
        # Arrange
        input = {'password': 'Strong_Password', 'username': 'test'}
        # Act
        response = client.post('/api/users', json=input)
        body = loads(response.data.decode('utf-8'))
        # Assert
        assert response.status_code == 400 and body == {'errors': {
            'password': "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_`"}, 'message': 'invalid data'}

    def test_post_method_with_valid_data_so_it_returns_201_created(self, client: FlaskClient):
        # Arrange
        input = {'password': 'Strong_Password2', 'username': 'test'}
        # Act
        response = client.post('/api/users', json=input)
        # Assert
        assert response.status_code == 201

    @patch('server.app.UserValidator')
    # def test_post_method_to_see_if_it_returns_500_internal_error_in_case_of_an_exception(self,client:FlaskClient,mock_user_validator):
    def test_users_post_method_to_see_if_it_returns_500_internal_error_in_case_of_an_exception(self, mock_user_validator: MagicMock, client: FlaskClient):
        # Arrange
        input = {'password': 'internal', 'username': 'error'}
        mock_user_validator.side_effect = Exception('testing')
        # Act
        response = client.post('/api/users', json=input)
        # Assert
        mock_user_validator.assert_called_once()
        assert response.status_code == 500

    def test_get_user_by_username_endpoint_so_it_returns_200_status_code(self, client: FlaskClient):
        # Arrange
        username = "toastedguy2"
        input = {'password': '_Byakuran4', 'username': username}
        client.post('/api/users', json=input)
        # Act
        response = client.get(f"/api/users/{username}")
        # Assert
        assert response.status_code == 200

    def test_get_user_by_username_endpoint_so_it_returns_404_status_code(self, client: FlaskClient):
        # Arrange
        username = "toastedguy2"
        # Act
        response = client.get(f"/api/users/{username}")
        # Assert
        assert response.status_code == 404

    @patch('server.app.UserRepository', side_effect=Exception())
    def test_get_user_by_username_endpoint_so_it_returns_500_status_code(elf, mock_user_repository: MagicMock, client: FlaskClient):
        # Arrange
        username = "toastedguy2"
        # Act
        response = client.get(f"/api/users/{username}")
        # Assert
        mock_user_repository.assert_called_once()
        assert response.status_code == 500

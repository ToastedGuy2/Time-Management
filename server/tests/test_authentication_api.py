import json
from flask.testing import FlaskClient
from unittest.mock import MagicMock, patch
from pytest import fixture
from ..app import app
from ..app import db
from json import loads


class TestAuthenticationApi():
    @fixture
    def client(self):
        app.app_context().push()
        db.drop_all()
        db.create_all()
        return app.test_client()

    def test_login_with_invalid_data_so_it_returns_400_BAD_REQUEST_status_code(self, client: FlaskClient):
        # Arrage
        none_data = None
        empty_dict = {}
        user_dict_with_empty_fields = {'password': '', 'username': ''}
        # Act
        response_to_none_data = client.post(
            '/api/authentication', json=none_data)
        body_response_to_none_data = loads(
            response_to_none_data.data.decode('utf-8'))
        response_to_empty_dict = client.post(
            '/api/authentication', json=empty_dict)
        body_response_to_empty_dict = loads(
            response_to_empty_dict.data.decode('utf-8'))
        response_to_user_dict_with_empty_fields = client.post(
            '/api/authentication', json=user_dict_with_empty_fields)
        body_response_to_user_dict_with_empty_fields = loads(
            response_to_user_dict_with_empty_fields.data.decode('utf-8'))
        # Assert
        assert response_to_none_data.status_code == 400 and body_response_to_none_data == {
            'message': "Please provide a json object"}
        assert response_to_none_data.status_code == 400 and body_response_to_empty_dict == {'errors': {
            'password': 'required field', 'username': 'required field'}, 'message': 'invalid data'}
        assert response_to_none_data.status_code == 400 and body_response_to_user_dict_with_empty_fields == {'errors': {
            'password': 'empty values not allowed', 'username': 'empty values not allowed'}, 'message': 'invalid data'}

    def test_login_with_an_invalid_username_password_so_it_returns_400_BAD_REQUEST_status_code(self, client: FlaskClient):
        # Arrage
        # Register User
        input = {'password': 'Strong_Password2', 'username': 'test'}
        # Act
        response = client.post('/api/authentication', json=input)
        body = loads(response.data.decode('utf-8'))
        # Assert
        assert response.status_code == 400 and body == {'message': "invalid data", 'errors': {
            'username': "there's no account registered with this username"}}

    def test_login_with_an_invalid_username_password_so_it_returns_400_BAD_REQUEST_status_code(self, client: FlaskClient):
        # Arrage
        # Register User
        user_to_create = {'password': 'Strong_Password2', 'username': 'test'}
        client.post('/api/users', json=user_to_create)
        input_for_login = {'password': 'Strong_Password', 'username': 'test'}
        # Act
        response = client.post('/api/authentication', json=input_for_login)
        body = loads(response.data.decode('utf-8'))
        # Assert
        assert response.status_code == 400 and body == {
            'message': "invalid password"}

    def test_login_with_valid_data_so_it_returns_200_OK_status_code(self, client: FlaskClient):
        # Arrage
        # Register User
        input = {'password': 'Strong_Password2', 'username': 'test'}
        client.post('/api/users', json=input)
        # Act
        response = client.post('/api/authentication', json=input)
        # Assert
        assert response.status_code == 200 and response.headers['Authentication'] != None

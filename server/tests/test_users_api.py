from flask.testing import FlaskClient
from unittest.mock import MagicMock, patch 
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
    def test_post_method_with_empty_dict_so_it_returns_400_bad_request(self,client:FlaskClient):
        # Arrange
        input = {}
        # Act
        response = client.post('/api/users',json=input)
        body = loads(response.data.decode('utf-8')) 
        # Assert
        assert response.status_code == 400 and body == {'errors':{'password':'required field','username':'required field'},'message':'invalid data'}
    def test_post_method_with_empty_fields_so_it_returns_400_bad_request(self,client:FlaskClient):
        # Arrange
        input = {'password':'','username':''}
        # Act
        response = client.post('/api/users',json=input)
        body = loads(response.data.decode('utf-8')) 
        # Assert
        assert response.status_code == 400 and body == {'errors':{'password':'empty values not allowed','username':'empty values not allowed'},'message':'invalid data'}
    def test_post_method_by_trying_to_post_same_input_twice_so_it_must_return_400_bad_request_since_user_is_already_created(self,client:FlaskClient):
        # Arrange
        input = {'password':'Strong_Password2','username':'test'}
        # Act
        client.post('/api/users',json=input)
        response = client.post('/api/users',json=input)
        # Assert
        assert response.status_code == 400
    def test_post_method_by_including_input_with_an_invalid_password_so_it_returns_400_bad_request(self,client:FlaskClient):
        # Arrange
        input = {'password':'Strong_Password','username':'test'}
        # Act
        response = client.post('/api/users',json=input)
        body = loads(response.data.decode('utf-8')) 
        # Assert
        assert response.status_code == 400 and body == {'errors':{'password': "Your password must contain at least:\n8 characters.\nOne uppercase letter.\nOne lowercase letter.\nOne number.\nOne special character like: @%+\/'!#$^?:.(){[]}~-_`"},'message':'invalid data'}
    def test_post_method_with_valid_data_so_it_returns_201_created(self,client:FlaskClient):
        # Arrange
        input = {'password':'Strong_Password2','username':'test'}
        # Act
        response = client.post('/api/users',json=input)
        # Assert
        assert response.status_code == 201
    # @patch('..app.UserValidator')
    # def test_post_method_to_see_if_it_returns_500_internal_error_in_case_of_an_exception(self,client:FlaskClient,mock_user_validator):
    def test_post_method_to_see_if_it_returns_500_internal_error_in_case_of_an_exception(self,client:FlaskClient):
        # Arrange
        with patch('server.app.UserValidator') as uv:
            input = {'password':'internal','username':'error'}
            uv.side_effect = ValueError('testing')
            # Act
            response = client.post('/api/users',json=input)
            # Assert
            uv.assert_called_once()
            assert response.status_code == 500
        
        
        
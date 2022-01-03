from pytest import fixture
from werkzeug.test import Client
from ..app import app
app.testc
class TestUsersApi():
    @fixture
    def client(self):
        return Client(app)
    def test_register_user(self,client:Client):
        response = client.post('/api/users',{})
        assert response is not None
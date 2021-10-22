import unittest.mock as mock
from ..shared.database import db
from ..models.User import User


class UserRepository:

    def get_by_id(self, id):
        return User.query.get(id)

    @mock.create_autospec
    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def insert(self, user):
        db.session.add(user)

    def is_there_an_user_with_such_username(self, username):
        return self.get_by_username(username) is not None

    def save_changes(self):
        db.session.commit()

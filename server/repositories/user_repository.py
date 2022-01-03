from ..shared.database import db
from ..models.User import User

class UserRepository:

    def get_by_id(self, id):
        return User.query.get(id)

    def get_by_username(self, username):
        return User.query.filter_by(username=username.lower()).first()

    def insert(self, user):
        db.session.add(user)

    def does_user_exist(self, username):
        return self.get_by_username(username) is not None

    def save_changes(self):
        db.session.commit()

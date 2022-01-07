from ..shared.database import db
from ..models.User import User

class UserRepository:

    def get_by_id(self, id)->User:
        return User.query.get(id)

    def get_by_username(self, username) ->User:
        return User.query.filter_by(username=username.lower()).first()

    def insert(self, user) ->None:
        db.session.add(user)

    def does_user_exist(self, username)->bool:
        return self.get_by_username(username) is not None

    def save_changes(self) ->None:
        db.session.commit()

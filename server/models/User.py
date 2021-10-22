from ..shared.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def asdict(self):
        return {'id': self.id, 'username': self.username, 'password': self.password}

    def __repr__(self):
        return '<User %r>' % self.username

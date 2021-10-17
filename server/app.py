from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask.json import jsonify
from .model.hasher import Hasher
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/pomodoro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/api/users", methods=["POST"])
def sign_up():
    model = request.json
    password = model["password"]
    password = Hasher().hash_password(password)
    username = model["username"]
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    userDictionary = {'username': username, 'password': password}
    return jsonify(userDictionary)

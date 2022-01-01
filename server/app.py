from flask import Flask, request
from flask.json import jsonify
# FLASK
from .utils.hasher import Hasher
from .utils.validations.user.user_validator import UserValidator
from .shared.database import db
from .models.User import User
from .repositories.user_repository import UserRepository
# from .utils.user_model import User
# PYTHON SHELL
# from model.hasher import Hasher
# from model.validations.user.user_validator import UserValidator

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/pomodoro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# TODO: TRY CATCH -> Document is Missing
@app.route("/api/users", methods=["POST"])
def sign_up():
    model = request.json
    v = UserValidator()
    if not v.is_user_valid(model):
        return {'message': "invalid data", 'errors': v.get_errors()}, 400
    repository = UserRepository()
    if repository.does_user_exist(model['username']):
        return {'message': "invalid data", 'errors': {'username': "username already taken"}}, 400
    password = model["password"]
    hash_password = Hasher().hash_password(password)
    lowercase_username = str.lower((model["username"]))
    user = User(username=lowercase_username, password=hash_password)
    repository.insert(user)
    repository.save_changes()
    user_dict = user.asdict()
    user_dict['url'] = f"http://127.0.0.1:5000/api/users/{user_dict['id']}"
    user_dict['password'] = model['password']
    return jsonify(user_dict)

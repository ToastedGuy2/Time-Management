from crypt import methods
from flask import Flask, request
from flask import Response
from jwt import encode
# FLASK
from .utils.hasher import Hasher
from .utils.validations.user.user_validator import UserValidator
from .shared.database import db
from .models.User import User
from .repositories.user_repository import UserRepository
# PYTHON SHELL
# from shared.database import db
# from models.User import User
secret_key = "Trend5-Isolation-Lived"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://toastedguy2:_Byakuran4@localhost/pomodoro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# TODO: TRY CATCH -> Document is Missing
# Users


@app.route("/api/users", methods=["POST"])
def sign_up():
    try:
        model = request.json
        v = UserValidator()
        if not v.is_user_to_create_valid(model):
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
        return user_dict, 201
    except ValueError as e:
        return {'message': "Please provide a json object"}, 400
    except Exception as e:
        return {'message': "Something went wrong while processing your request"}, 500

# TODO: TRY CATCH -> Document is Missing


@app.route("/api/authentication", methods=["POST"])
def login():
    try:
        model = request.json
        v = UserValidator()
        if not v.is_user_to_login_valid(model):
            return {'message': "invalid data", 'errors': v.get_errors()}, 400
        repository = UserRepository()
        user = repository.get_by_username(model['username'])
        if user is None:
            return {'message': "invalid data", 'errors': {'username': "there's no account registered with this username"}}, 400
        password = model["password"]
        if(Hasher().verify_password(password, user.password)):
            payload = {'id': user.id, 'username': user.username}
            encoded = encode(payload, secret_key)
            return Response(headers={'Authentication': f"Bearer {encoded}"})
        else:
            return {'message': "invalid password"}, 400
    except ValueError as e:
        return {'message': "Please provide a json object"}, 400
    except Exception as e:
        return {'message': "Something went wrong while processing your request"}, 500
# Users


@app.route("/api/users/<username>", methods=['GET'])
def get_user_by_username(username):
    user = UserRepository().get_by_username(username).asdict()
    del user["password"]
    if user is None:
        return {"message": "The user you're looking for doesn't exist"}, 404
    return {"data": user}, 200

import datetime
from werkzeug.security import safe_str_cmp, check_password_hash
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token


from ..model import User


class SignUp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('email', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('password', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('confirm_password', type=str, required=True,
                        help="This field cannot be left blank")

    def post(self):
        ''' Add a new user '''
        data = SignUp.parser.parse_args()

        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']

        user = User()

        if user.get_by_username(username):
            return {'message': 'User exists'}, 400
        if user.get_by_email(email):
            return {'message': 'User exists'}, 400
        if not safe_str_cmp(password, confirm_password):
            return {'message': 'passwords do not match'}, 400

        user = User(username, email, password, confirm_password)

        user.add()

        return {'message': 'successfully created a new account'}, 201


class Login(Resource):

    def post(self):
        ''' login a user '''
        data = SignUp.parser.parse_args()

        username = data['username']
        password = data['password']

        user = User()

        if not user.get_by_username(username):
            return {'message': 'user does not exist'}, 404

        if not check_password_hash(user.password, password):
            return {'message': 'Wrong password'}, 400

        token = create_access_token(
            user.username)
        return{'token': token, 'meassage': f'Successfully login in{username}'}, 200

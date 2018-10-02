'''import modules'''
from werkzeug.security import check_password_hash
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token


from app.api.v2.model import User
from utils.validators import Validators


class SignUp(Resource):
    ''' method for signing up a user'''
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('email', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('password', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('confirmpassword', type=str, required=True,
                        help="This field cannot be left blank")

    def post(self):
        ''' Add a new user '''
        data = SignUp.parser.parse_args()

        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']

        if not Validators().valid_username(username):
            return {'message': 'Enter valid username'}, 400
        if not Validators().valid_password(password):
            return {'message': 'Enter valid password'}, 400
        if User().get_by_username(username):
            return {'message': 'Username exists'}, 409
        if User().get_by_email(email):
            return {'message': 'Email address exists'}, 409

        user = User(username, email, password, confirm_password)

        user.add()

        return {'message': 'successfully created a new account'}, 201


class Login(Resource):
    ''' method for a user to login'''
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help="This field cannot be left blank")
    parser.add_argument('password', type=str, required=True,
                        help="This field cannot be left blank")

    def post(self):
        ''' login a user '''
        data = Login.parser.parse_args()

        username = data['username']
        password = data['password']

        user = User().get_by_username(username)

        if not user:
            return {'message': 'user does not exist'}, 404

        if not check_password_hash(user.password, password):
            return {'message': 'Wrong password'}, 400

        token = create_access_token(
            identity=user.serialize())

        return {
            'token': token,
            'message': 'successfully logged in'
            }, 200

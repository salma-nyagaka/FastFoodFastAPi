'''module imports'''
from flask import Blueprint


from .auth import SignUp, Login

AUTH_BLUEPRINT = Blueprint('auth', __name__)

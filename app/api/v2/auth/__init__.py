'''module imports'''
from flask import Blueprint


from .auth import SignUp, Login, UpdateProfile


AUTH_BLUEPRINT = Blueprint('auth', __name__)

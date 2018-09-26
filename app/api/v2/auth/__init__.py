from flask import Blueprint
from .auth import SignUp, Login 


auth_blueprint = Blueprint('auth', __name__)
from flask import Blueprint
from flask import Blueprint


from .admin import *


admin_blueprint = Blueprint('admin', __name__)

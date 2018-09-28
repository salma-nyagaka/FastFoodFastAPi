from flask import Blueprint
from .users import AllOrders, PlaceNewOrder, AllMenu


user_blueprint = Blueprint('user', __name__)

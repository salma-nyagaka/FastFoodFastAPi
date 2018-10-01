from flask import Blueprint
from .users import GetOrders, PlaceOrder


user_blueprint = Blueprint('user', __name__)

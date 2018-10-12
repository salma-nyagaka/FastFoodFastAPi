'''module imports'''
from flask import Blueprint


from .users import GetOrders, PlaceOrder, GetAllMenu


USER_BLUEPRINT = Blueprint('user', __name__)

'''module imports'''
from flask import Blueprint


from .users import GetOrders, PlaceOrder, GetAllMenu, GetNewOrders, DeleteOrder


USER_BLUEPRINT = Blueprint('user', __name__)

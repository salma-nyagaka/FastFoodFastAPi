''' blueprint for admin routes'''
from flask import Blueprint


from .admin import (PlaceNewMenu, AllMenu, SpecificMenu, AcceptOrder, CompleteOrder,
                    GetSpecificOrder, AllUserOrders)


ADMIN_BLUEPRINT = Blueprint('admin', __name__)

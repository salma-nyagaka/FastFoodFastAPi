''' blueprint for admin routes'''
from flask import Blueprint


from .admin import (PlaceNewMenu, AllMenu, SpecificMenu,
                    GetSpecificOrder, AllUserOrders, UpdateStatus)


ADMIN_BLUEPRINT = Blueprint('admin', __name__)

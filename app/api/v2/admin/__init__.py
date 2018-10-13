''' blueprint for admin routes'''
from flask import Blueprint


from .admin import (PlaceNewMenu, AllMenu, SpecificMenu, DeleteMenu, UpdateStatus,
                    GetSpecificOrder, AllUserOrders, UpdateStatus, FilterOrdersByStatus,
                    UpdateMeal)


ADMIN_BLUEPRINT = Blueprint('admin', __name__)

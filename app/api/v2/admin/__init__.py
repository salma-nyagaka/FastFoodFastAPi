''' module imports'''
from flask import Blueprint

from .admin import (PlaceNewMenu, AllMenu, SpecificMenu, AllUserOrders,
                    GetSpecificOrder, AcceptOrder, CompleteOrder, DeclineOrder)


ADMIN_BLUEPRINT = Blueprint('admin', __name__)

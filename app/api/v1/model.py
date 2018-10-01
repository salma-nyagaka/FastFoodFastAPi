orders = []


class FoodOrder:

    def __init__(self, name=None, price=None,
                 description=None, status="Pending"):
        self.id = len(orders)+1
        self.name = name
        self.price = price
        self.description = description
        self.status = status

    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            status=self.status
        )

    def get_id(self, order_id):
        for order in orders:
            if order.id == order_id:
                return order

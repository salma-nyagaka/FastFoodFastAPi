
orders = []
class FoodOrder:
    

    order_id = 1
    def __init__(self,name=None,price=None,description=None, status="Pending"):
        self.id=FoodOrder.order_id
        self.name=name
        self.price=price
        self.description=description
        self.status=status
        

        FoodOrder.order_id += 1

    
    
    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            status=self.status
        )

    def get_by_id(self, order_id):
        for order in orders:
            if order.id == order_id:
                return order
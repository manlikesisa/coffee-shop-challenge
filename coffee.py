class Coffee :
    def__init__(self,name)
    if not isinstance(name,str):
        raise TypeError("Name must be a string")
        if len(name) <3:
         raise ValueError("Name must be at least 3 characters long")
    self.name = name



@property
   def name(self):
    return self.name

    def orders(self):
        return [order for order in Order._all_orders if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        all_orders = self.orders()
        if not all_orders:
            return 0
        total_price = sum(order.price for order in all_orders)
        return total_price / len(all_orders)

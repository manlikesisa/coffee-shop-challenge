class Customer :
    def__init__(self,name):
    self.name = name



   @property
   def name(self):
   return self.name:

    @name.setter
   def name(self,value):
    if isinstance(value, str) and 1<= len(value) <=15:
        self.name = value
        else:
            raise ValueError ("Name should be between 1 and 15 characters")
            self.name = value

    def orders(self):
        return [order for order in Order._all_orders if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    
    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Expected a Coffee instance.")

        customer_spending = {}

        for order in Order._all_orders:
            if order.coffee is coffee:
                customer_spending[order.customer] = (
                    customer_spending.get(order.customer, 0) + order.price
                )

        if not customer_spending:
            return None

        return max(customer_spending, key=customer_spending.get)
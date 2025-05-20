class Order :
    _all_orders = []

    def__init__(self,customer,coffee,price)
     if not isinstance(customer,Customer):
        raise TypeError("customer must be an istance of Customer")
     if not isistance(coffee,Coffee):
        raise TypeError("coffee must be an istance of Coffee")
     if not isistance(price,float):
        raise TypeError("price must be a float")
     if not (1.0 <= price <= 10.0):
        raise ValueError("price must be between 1.0 and 10.0")


         self.customer = customer
         self.coffee = coffee
         self.price = price

       order._all_orders.append(self)

    @property
    def customer(self):
       return self.customer

       @property
       def coffee(self):
        return self._coffee

   @property
   def price(self):
       return self.price
# coffee-shop-challenge
This is a project that models a coffee shop ordering system. It uses three main classes: Customer, Coffee, and Order to keep track of who is ordering what, and how much they're spending.

How it Works:
Customer: Has a name and can place orders.

Coffee: Each coffee has a name and can be ordered by different customers.

Order: Connects a customer to a coffee with a price.

All orders are stored and used to get stats like who orders the most of a certain coffee, how many times a coffee has been ordered, etc.

Features
Customer
Can only have a name between 1 and 15 characters.

Can place an order for a coffee with a price.

Can view all their orders.

Can see which different coffees they've ordered.

Can check who spent the most on a specific coffee (most_aficionado method).

Coffee
Name must be at least 3 characters long.

Can return all its orders.

Can list all customers who ordered it.

Can count how many times it's been ordered.

Can calculate its average order price.

Order
Needs a valid Customer, Coffee, and a price (between 1.0 and 10.0).

Keeps track of all orders in a class variable.

Has read-only access to the customer, coffee, and price.


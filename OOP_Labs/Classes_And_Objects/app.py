"""Class for categorizing different tasks to be run as part of the application

Each subgroup of tasks for a particular topic will be part of a separate method.
These methods can be called individually to execute a set of related tasks at once
"""

from alarm_clock import AlarmClock
from product import Product
from customer import Customer

class App:
    """Defines the types of tasks the application can perform
    
    Public Static Methods:
        alarm_clock_tasks:
            Runs a set of tasks related to creating, inspecting, and configuring an alarm clock
        shopping_cart_tasks:
            Runs a set of tasks related to creating customers, products, and their interactions via a shopping cart
    """
    def alarm_clock_tasks(self):
        """Runs a set of tasks related to creating, inspecting, and configuring an alarm clock

        Effects:
            Console display of task type and clock times
        """
        print('\nAlarm Clock Tasks:')
        alarm_clock = AlarmClock()
        print(alarm_clock.current_time)
        alarm_clock.set_current_time()
        alarm_clock.set_is_alarm_enabled()

    def shopping_cart_tasks(self):
        """Runs a set of tasks related to creating customers, products, and their interactions via a shopping cart

        Effects:
            Console display of task type, customer name, products in cart, and cart total price
        """
        print('\nShopping Cart Tasks:')
        customer = Customer('Mark Watney')
        product_one = Product('Bag Of Potatos', 10.50, 'Food')
        product_two = Product('Space Suit Helmet', 17975.00, 'Capital Equipment')
        product_three = Product('Duct Tape', 4.99, 'Equipment')

        print(customer.name)
        customer.add_product_to_customer_cart(product_one)
        customer.add_product_to_customer_cart(product_two)
        customer.add_product_to_customer_cart(product_three)
        customer.display_cart()
        cart_total = customer.shopping_cart.current_products_total_price()
        print(f'\nThe current cart total is: {cart_total}')
        customer.shopping_cart.clear_cart()
        customer.display_cart()
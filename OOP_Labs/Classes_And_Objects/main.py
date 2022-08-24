from alarm_clock import AlarmClock
from product import Product
from customer import Customer

def main():
    alarm_clock_tasks()
    shopping_cart_tasks()

def alarm_clock_tasks():
    print('\nAlarm Clock Tasks:')
    alarm_clock = AlarmClock()
    print(alarm_clock.current_time)
    alarm_clock.set_current_time()
    alarm_clock.set_is_alarm_enabled()

def shopping_cart_tasks():
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

main()
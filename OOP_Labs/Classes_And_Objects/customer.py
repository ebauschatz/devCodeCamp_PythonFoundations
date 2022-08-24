from shopping_cart import ShoppingCart

class Customer:
    '''Representation of a customer who will purchase items

    Instance Variables:
        name -- string representing the name of the customer
        shopping_cart -- shopping cart object associated with the customer

    Public Methods:
        add_product_to_customer_cart:
            Adds a single product object to the cart via a method on the cart object
            Parameters:
                new_product -- a single product object to add to the cart
            Effects:
                The new product is appended to the existing cart
        display_cart:
            Prints the contents of the cart to the console, or a message if the cart is empty
    '''
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_product_to_customer_cart(self, new_product):
        self.shopping_cart.add_product_to_cart(new_product)

    def display_cart(self):
        if len(self.shopping_cart.products) == 0:
            print('\nThe shopping cart is currently empty.')
        else:
            for product in self.shopping_cart.products:
                print(f'\nProduct Name: {product.name}')
                print(f'Product Price: {product.price}')
                print(f'Product Category: {product.category}')
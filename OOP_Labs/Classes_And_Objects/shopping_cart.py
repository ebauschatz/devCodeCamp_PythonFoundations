class ShoppingCart:
    '''A collection of products that a customer intends to purchase

    Instance Variables:
        products - a list of Product objects

    Public Methods:
        current_products_total_price:
            Calculate the sum of all prices from all product objects in the cart
            Returns:
                float of the price total
        add_product_to_cart:
            Appends a new product object to the current product list
            Parameters:
                new_product -- a product object to append
            Effects:
                The new product will be appended to the existing products list
        clear_cart:
            Removes all products from the cart
            Effects:
                Resets the products list to an empty list
    '''
    def __init__(self):
        self.products = []

    def current_products_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        return total_price

    def add_product_to_cart(self, new_product):
        self.products.append(new_product)

    def clear_cart(self):
        self.products = []
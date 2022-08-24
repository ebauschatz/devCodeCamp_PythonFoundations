class Product:
    '''Describes an individual product that can be purchased.

    Instance Variables:
        name -- string of the product's externally visible name
        price -- float for the current product price
        category -- string representing the product's classification
    '''
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
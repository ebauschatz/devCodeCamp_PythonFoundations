"""Class file for Products.

This class will be used to represent a physical product that can be purchased.
"""

class Product:
    """Describes an individual product that can be purchased.

    Instance Variables:
        name -- string of the product's externally visible name
        price -- float for the current product price
        category -- string representing the product's classification
    """
    def __init__(self, name, price, category):
        """Initializes a product object

        Instance Variables from Parameters:
            name:
                string of the product's externally visible name
            price :
                float for the current product price
            category:
                string representing the product's classification
        """
        self.name = name
        self.price = price
        self.category = category
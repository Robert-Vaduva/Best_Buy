"""
Product management module.

Defines the Product class for representing store items with attributes
such as name, price, quantity, and active status. Provides methods for
inventory management, product activation/deactivation, displaying product
details, and processing purchases.
"""


class Product:
    """
    Represents a product with a name, price, quantity, and active status.
    Provides methods to manage inventory, update status, display details,
    and process purchases.
    """
    def __init__(self, name, price, quantity):
        """Initialize a product with name, price, and quantity."""
        try:
            self.name = str(name)
            if self.name == "":
                raise ValueError("Product name cannot be empty")
            self.price = float(price)
            if self.price < 0 or any(elem.isalpha() for elem in str(price)):
                raise ValueError("Invalid price, please provide a real number, "
                                 "greater than zero")
            self.quantity = int(quantity)
            if self.quantity < 0 or any(elem.isalpha() for elem in str(quantity)):
                raise ValueError("Invalid quantity, please provide a real number, "
                                 "greater or equal to zero")
            self.active = True
        except (TypeError, ValueError) as error:
            print(error)

    def get_quantity(self):
        """Return the current quantity in stock."""
        return int(self.quantity)

    def set_quantity(self, quantity):
        """Update the product quantity and deactivate if it reaches zero."""
        try:
            self.quantity = int(quantity)
            if self.quantity < 0 or any(elem.isalpha() for elem in str(quantity)):
                raise ValueError("Invalid quantity, please provide a real number, "
                                 "greater or equal to zero")
            if self.quantity == 0:
                self.active = False
        except (TypeError, ValueError) as error:
            print(error)

    def is_active(self):
        """Return True if the product is active, else False."""
        return self.active is True

    def activate(self):
        """Mark the product as active."""
        self.active = True

    def deactivate(self):
        """Mark the product as inactive."""
        self.active = False

    def show(self):
        """Display product details (name, price, quantity)."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """Reduce stock by given quantity and return total price."""
        self.quantity -= quantity
        return self.price * quantity


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

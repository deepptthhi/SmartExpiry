from datetime import datetime


class Item:
    """
    Represents a generic inventory item.

    All specific item types such as Medicine, Grocery,
    and Document inherit from this class.
    """

    def __init__(self, item_id, name, category, quantity, expiry_date):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.expiry_date = expiry_date

    def days_left(self):
        """
        Calculate and return the number of days left
        until the item expires.
        """

        today = datetime.today().date()
        expiry = datetime.strptime(self.expiry_date, "%d-%m-%Y").date()

        return (expiry - today).days

    def is_expired(self):
        """
        Check whether the item has already expired.
        """

        return self.days_left() < 0

    def display(self):
        """
        Display the common details of an inventory item.
        """

        print(f"ID        : {self.item_id}")
        print(f"Name      : {self.name}")
        print(f"Category  : {self.category}")
        print(f"Quantity  : {self.quantity}")
        print(f"Expiry    : {self.expiry_date}")
        print(f"Days Left : {self.days_left()}")
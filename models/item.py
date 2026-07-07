from datetime import datetime


class Item:
    """
    Base class for every inventory item.
    """

    def __init__(self, item_id, name, category, quantity, expiry_date):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.expiry_date = expiry_date

    def days_left(self):
        """
        Returns the number of days left until the expiry.
        """

        today = datetime.today().date()
        expiry = datetime.strptime(self.expiry_date, "%d-%m-%Y").date()

        return (expiry - today).days

    def is_expired(self):
        """
        Returns True if the item has expired.
        """

        return self.days_left() < 0

    def display(self):
        """
        Displays item details.
        """

        print(f"""
ID        : {self.item_id}
Name      : {self.name}
Category  : {self.category}
Quantity  : {self.quantity}
Expiry    : {self.expiry_date}
Days Left : {self.days_left()}
""")
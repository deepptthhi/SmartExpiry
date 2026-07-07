from models.item import Item


class Grocery(Item):

    def __init__(self, item_id, name, quantity, expiry_date, weight):

        super().__init__(
            item_id,
            name,
            "Grocery",
            quantity,
            expiry_date
        )

        self.weight = weight

    def display(self):

        super().display()

        print(f"Weight    : {self.weight}")
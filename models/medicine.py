from models.item import Item


class Medicine(Item):

    """
    Represents a medicine item.
    """

    def __init__(self, item_id, name, quantity, expiry_date, manufacturer, dosage):

        super().__init__(
            item_id,
            name,
            "Medicine",
            quantity,
            expiry_date
        )

        self.manufacturer = manufacturer
        self.dosage = dosage


    """
    Display medicine details.
    """   
    
    def display(self):

        super().display()

        print(f"Manufacturer : {self.manufacturer}")
        print(f"Dosage       : {self.dosage}")
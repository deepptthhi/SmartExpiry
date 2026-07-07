from models.item import Item


class Medicine(Item):

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

    def display(self):

        super().display()

        print(f"""Manufacturer : {self.manufacturer}
Dosage       : {self.dosage}
""")
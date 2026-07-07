from models.item import Item


class Document(Item):

    def __init__(self, item_id, name, quantity, expiry_date, issued_by):

        super().__init__(
            item_id,
            name,
            "Document",
            quantity,
            expiry_date
        )

        self.issued_by = issued_by

    def display(self):

        super().display()

        print(f"Issued By : {self.issued_by}")
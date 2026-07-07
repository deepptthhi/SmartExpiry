from models.medicine import Medicine
from models.grocery import Grocery
from models.documents import Document

from services.inventory import Inventory


def main():

    inventory = Inventory()

    medicine = Medicine(
        1,
        "Paracetamol",
        10,
        "20-07-2026",
        "Cipla",
        "500 mg"
    )

    grocery = Grocery(
        2,
        "Rice",
        2,
        "25-12-2026",
        "5 kg"
    )

    document = Document(
        3,
        "Passport",
        1,
        "20-01-2030",
        "Government of India"
    )

    inventory.add_item(medicine)
    inventory.add_item(grocery)
    inventory.add_item(document)

    print("\nBefore deleting:\n")
    inventory.view_items()
    
    inventory.delete_item(2)
    print("\nAfter deleting:\n")
    inventory.view_items()
    inventory.save_items()


if __name__ == "__main__":
    main()
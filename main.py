from services.inventory import Inventory

from models.medicine import Medicine
from models.grocery import Grocery
from models.documents import Document


def create_item():

    print("\nChoose Category")
    print("1. Medicine")
    print("2. Grocery")
    print("3. Document")

    category = input("\nEnter your choice: ")

    item_id = int(input("Item ID: "))
    name = input("Item Name: ")
    quantity = int(input("Quantity: "))
    expiry = input("Expiry Date (DD-MM-YYYY): ")

    if category == "1":

        manufacturer = input("Manufacturer: ")
        dosage = input("Dosage: ")

        return Medicine(
            item_id,
            name,
            quantity,
            expiry,
            manufacturer,
            dosage
        )

    elif category == "2":

        weight = input("Weight: ")

        return Grocery(
            item_id,
            name,
            quantity,
            expiry,
            weight
        )

    elif category == "3":

        issued_by = input("Issued By: ")

        return Document(
            item_id,
            name,
            quantity,
            expiry,
            issued_by
        )

    else:

        print("\nInvalid category.")

        return None
    

def display_menu():

    print("\n" + "=" * 45)
    print("📦              SmartExpiry")
    print("=" * 45)

    print("1. Add Item")
    print("2. View Items")
    print("3. Search Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Check Expiry")
    print("7. Exit")

    print("=" * 45)


def main():

    inventory = Inventory()
    inventory.load_items()

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\n" + "-" * 45)

            item = create_item()

            if item:
                inventory.add_item(item)
                inventory.save_items()

        elif choice == "2":

            print("\n" + "-" * 45)

            inventory.view_items()

        elif choice == "3":

            print("\n" + "-" * 45)

            name = input("Enter item name: ")

            item = inventory.search_item(name)

            if item:
                print("\n Item Found!\n")
                item.display()
            else:
                print("\n Item not found.")

        elif choice == "4":

            print("\n" + "-" * 45)

            item_id = int(input("Enter Item ID: "))

            inventory.delete_item(item_id)
            inventory.save_items()

        elif choice == "5":

            print("\n" + "-" * 45)

            item_id = int(input("Enter Item ID: "))

            inventory.update_item(item_id)
            inventory.save_items()

        elif choice == "6":

            print("\n" + "-" * 45)

            inventory.check_expiry()

        elif choice == "7":

            inventory.save_items()

            print("\n" + "=" * 45)
            print(" Thank you for using SmartExpiry!")
            print("Have a great day!")
            print("=" * 45)

            break

        else:

            print("\n Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
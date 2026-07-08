from services.inventory import Inventory


def display_menu():

    print("\n" + "=" * 40)
    print("📦 SmartExpiry")
    print("=" * 40)
    print("1. View Items")
    print("2. Check Expiry")
    print("3. Exit")


def main():

    inventory = Inventory()

    inventory.load_items()

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":

            inventory.view_items()

        elif choice == "2":

            inventory.check_expiry()

        elif choice == "3":

            inventory.save_items()

            print("\nThank you for using SmartExpiry!")

            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
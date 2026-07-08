from services.inventory import Inventory


def main():

    inventory = Inventory()

    inventory.load_items()

    print("\nBefore Update\n")

    inventory.view_items()

    inventory.update_item(1)

    print("\nAfter Update\n")

    inventory.view_items()

    inventory.save_items()


if __name__ == "__main__":
    main()
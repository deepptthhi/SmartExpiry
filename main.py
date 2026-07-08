from services.inventory import Inventory


def main():

    inventory = Inventory()

    inventory.load_items()

    inventory.view_items()


if __name__ == "__main__":
    main()
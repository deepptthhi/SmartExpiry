from models.item import Item


def main():

    item = Item(
        1,
        "Milk",
        "Grocery",
        2,
        "15-07-2026"
    )

    item.display()

    print("Expired:", item.is_expired())


if __name__ == "__main__":
    main()
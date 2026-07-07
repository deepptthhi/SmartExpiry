import json
import os


class Inventory:

    def __init__(self):
        self.items = []
        self.file_path = "data/inventory.json"

    # ------------------------
    # Add Item
    # ------------------------
    def add_item(self, item):
        self.items.append(item)
        print(f"\n'{item.name}' added successfully!")

    # ------------------------
    # View Items
    # ------------------------
    def view_items(self):

        if not self.items:
            print("\nInventory is empty.")
            return

        print("\n========== INVENTORY ==========\n")

        for item in self.items:
            item.display()
            print("-" * 40)

    # ------------------------
    # Search Item
    # ------------------------
    def search_item(self, name):

        for item in self.items:

            if item.name.lower() == name.lower():
                return item

        return None

    # ------------------------
    # Delete Item
    # ------------------------
    def delete_item(self, item_id):

        for item in self.items:

            if item.item_id == item_id:

                self.items.remove(item)

                print("\nItem deleted successfully!")

                return

        print("\nItem not found.")
    
    # ------------------------
    # Save Items
    # ------------------------

    def save_items(self):

        data = []

        for item in self.items:

            item_data = item.__dict__.copy()

            item_data["type"] = item.__class__.__name__

            data.append(item_data)

        with open(self.file_path, "w") as file:

            json.dump(data, file, indent=4)

        print("\nInventory saved successfully!")

    # ------------------------
    # Load Items
    # ------------------------

    def load_items(self):

        if not os.path.exists(self.file_path):

            return

        with open(self.file_path, "r") as file:

            data = json.load(file)

        print(f"\nLoaded {len(data)} item(s) from storage.")
import json
import os

from models.medicine import Medicine
from models.grocery import Grocery
from models.documents import Document

class Inventory:

    def __init__(self):
        self.items = []
        self.file_path = "data/inventory.json"

    
    # Add a new item to the inventory

    def add_item(self, item):
        self.items.append(item)
        print(f"\n'{item.name}' added successfully!")

    
    # Display all items
    
    def view_items(self):

        if not self.items:
            print("\nInventory is empty.")
            return

        print("\n========== INVENTORY ==========\n")

        for item in self.items:
            item.display()
            print()
            print("-" * 45)

    # Save inventory to JSON

    def search_item(self, name):

        for item in self.items:

            if item.name.lower() == name.lower():
                return item

        return None

    
    #Delete Item
   
    def delete_item(self, item_id):

        for item in self.items:

            if item.item_id == item_id:

                self.items.remove(item)

                print("\nItem deleted successfully!")

                return

        print("\nItem not found.")


    # Update Item
    

    def update_item(self, item_id):

        for item in self.items:

            if item.item_id == item_id:

                print(f"\nUpdating '{item.name}'")

                new_name = input("New Name (leave blank to keep same): ")

                if new_name:
                    item.name = new_name

                new_quantity = input("New Quantity (leave blank to keep same): ")

                if new_quantity:
                    item.quantity = int(new_quantity)

                new_expiry = input("New Expiry Date (DD-MM-YYYY, leave blank to keep same): ")

                if new_expiry:
                    item.expiry_date = new_expiry

                print("\nItem updated successfully!")

                return

        print("\nItem not found.")


    #Check Expiry
    
    def check_expiry(self):

        expired = []
        today = []
        soon = []
        safe = []

        for item in self.items:

            days = item.days_left()

            if days < 0:
                expired.append(item)

            elif days == 0:
                today.append(item)

            elif days <= 7:
                soon.append(item)

            else:
                safe.append(item)

        print("\n========== EXPIRY REPORT ==========\n")

        print("Expired:")

        if expired:
            for item in expired:
                print(f"- {item.name}")
        else:
            print("None")

        print("\n Expiring Today:")

        if today:
            for item in today:
                print(f"- {item.name}")
        else:
            print("None")

        print("\nExpiring Within 7 Days:")

        if soon:
            for item in soon:
                print(f"- {item.name} ({item.days_left()} day(s) left)")
        else:
            print("None")

        print("\nSafe:")

        if safe:
            for item in safe:
                print(f"- {item.name} ({item.days_left()} day(s) left)")
        else:
            print("None")
    
   
    #Save Items
  

    def save_items(self):

        data = []

        for item in self.items:

            item_data = item.__dict__.copy()

            item_data["type"] = item.__class__.__name__

            data.append(item_data)

        with open(self.file_path, "w") as file:

            json.dump(data, file, indent=4)

        print("\nInventory saved successfully!")


    #Load Items
    

    def load_items(self):

        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, "r") as file:
            data = json.load(file)

        self.items = []

        for item in data:

            item_type = item["type"]

            if item_type == "Medicine":

                obj = Medicine(
                    item["item_id"],
                    item["name"],
                    item["quantity"],
                    item["expiry_date"],
                    item["manufacturer"],
                    item["dosage"]
                )

            elif item_type == "Grocery":

                obj = Grocery(
                    item["item_id"],
                    item["name"],
                    item["quantity"],
                    item["expiry_date"],
                    item["weight"]
                )

            elif item_type == "Document":

                obj = Document(
                    item["item_id"],
                    item["name"],
                    item["quantity"],
                    item["expiry_date"],
                    item["issued_by"]
                )

            else:
                continue

            self.items.append(obj)

        print(f"\nLoaded {len(self.items)} item(s).")
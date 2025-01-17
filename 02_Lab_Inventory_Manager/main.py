import json
import os

# File to store inventory data
INVENTORY_FILE = "lab_inventory.json"

# Function to load inventory from the file
def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save inventory to the file
def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file, indent=4)

# Function to display the inventory
def display_inventory(inventory):
    if not inventory:
        print("\nNo equipment in inventory.\n")
        return
    print("\nCurrent Inventory:")
    print("-" * 30)
    for equipment, details in inventory.items():
        print(f"Name: {equipment}")
        print(f"  Quantity: {details['quantity']}")
        print(f"  Location: {details['location']}")
        print(f"  Notes: {details['notes']}")
        print("-" * 30)
    print()

# Function to add equipment
def add_equipment(inventory):
    name = input("Enter equipment name: ").strip()
    if name in inventory:
        print("Equipment already exists. Use update option to modify it.")
        return
    quantity = int(input("Enter quantity: "))
    location = input("Enter location: ").strip()
    notes = input("Enter any additional notes: ").strip()
    inventory[name] = {
        "quantity": quantity,
        "location": location,
        "notes": notes
    }
    print("Equipment added successfully!")

# Function to update equipment details
def update_equipment(inventory):
    name = input("Enter equipment name to update: ").strip()
    if name not in inventory:
        print("Equipment not found!")
        return
    print("Leave a field blank to retain the current value.")
    quantity = input(f"Enter new quantity (current: {inventory[name]['quantity']}): ").strip()
    location = input(f"Enter new location (current: {inventory[name]['location']}): ").strip()
    notes = input(f"Enter new notes (current: {inventory[name]['notes']}): ").strip()

    if quantity:
        inventory[name]["quantity"] = int(quantity)
    if location:
        inventory[name]["location"] = location
    if notes:
        inventory[name]["notes"] = notes
    print("Equipment updated successfully!")

# Function to delete equipment
def delete_equipment(inventory):
    name = input("Enter equipment name to delete: ").strip()
    if name in inventory:
        del inventory[name]
        print("Equipment deleted successfully!")
    else:
        print("Equipment not found!")

# Main menu function
def main():
    inventory = load_inventory()
    while True:
        print("\nLab Equipment Inventory Manager")
        print("1. View Inventory")
        print("2. Add Equipment")
        print("3. Update Equipment")
        print("4. Delete Equipment")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            add_equipment(inventory)
        elif choice == "3":
            update_equipment(inventory)
        elif choice == "4":
            delete_equipment(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
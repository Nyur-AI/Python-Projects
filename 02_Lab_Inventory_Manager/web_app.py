import streamlit as st
import pandas as pd
import json
import os

# File to store inventory data
INVENTORY_FILE = "lab_inventory.json"

# Load inventory data from the file
def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    return {}

# Save inventory data to the file
def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

# Convert inventory dictionary to a DataFrame
def inventory_to_dataframe(inventory):
    if not inventory:
        return pd.DataFrame(columns=["Name", "Quantity", "Location", "Notes"])
    data = [
        {"Name": name, "Quantity": details["quantity"], "Location": details["location"], "Notes": details["notes"]}
        for name, details in inventory.items()
    ]
    return pd.DataFrame(data)

# Streamlit App
def main():
    st.title("Lab Equipment Inventory Manager")

    # Load inventory data
    inventory = load_inventory()

    # Sidebar menu
    menu = st.sidebar.radio(
        "Choose an action",
        ["View Inventory", "Add Equipment", "Update Equipment", "Delete Equipment"]
    )

    # View Inventory
    if menu == "View Inventory":
        st.header("Current Inventory")
        inventory_df = inventory_to_dataframe(inventory)
        if inventory_df.empty:
            st.warning("No equipment in inventory.")
        else:
            st.dataframe(inventory_df)

    # Add Equipment
    elif menu == "Add Equipment":
        st.header("Add New Equipment")
        name = st.text_input("Equipment Name")
        quantity = st.number_input("Quantity", min_value=1, step=1)
        location = st.text_input("Location")
        notes = st.text_area("Notes")
        if st.button("Add Equipment"):
            if name in inventory:
                st.error("Equipment already exists. Use the update option to modify it.")
            else:
                inventory[name] = {
                    "quantity": quantity,
                    "location": location,
                    "notes": notes
                }
                save_inventory(inventory)
                st.success("Equipment added successfully!")

    # Update Equipment
    elif menu == "Update Equipment":
        st.header("Update Existing Equipment")
        name = st.selectbox("Select Equipment", list(inventory.keys()))
        if name:
            quantity = st.number_input(
                "Quantity", min_value=1, step=1, value=inventory[name]["quantity"]
            )
            location = st.text_input("Location", value=inventory[name]["location"])
            notes = st.text_area("Notes", value=inventory[name]["notes"])
            if st.button("Update Equipment"):
                inventory[name] = {
                    "quantity": quantity,
                    "location": location,
                    "notes": notes
                }
                save_inventory(inventory)
                st.success("Equipment updated successfully!")

    # Delete Equipment
    elif menu == "Delete Equipment":
        st.header("Delete Equipment")
        name = st.selectbox("Select Equipment", list(inventory.keys()))
        if st.button("Delete Equipment"):
            del inventory[name]
            save_inventory(inventory)
            st.success("Equipment deleted successfully!")

if __name__ == "__main__":
    main()
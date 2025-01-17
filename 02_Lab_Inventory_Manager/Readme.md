## Computer Lab Inventory Manager

A user-friendly web application built with Python and Streamlit to manage and track lab equipment inventory. This system allows users to easily add, view, update, and delete equipment records, making inventory management efficient and organized.

---

## Features

- **View Inventory**: Displays the inventory in an interactive **tabular format** for easy navigation and understanding.
- **Add Equipment**: Allows users to add new items to the inventory, specifying quantity, location, and additional notes.
- **Update Equipment**: Enables modification of existing inventory items with real-time updates.
- **Delete Equipment**: Provides a seamless option to remove outdated or unused equipment from the inventory.
- **Persistent Data Storage**: Uses JSON for reliable and structured data storage, ensuring information is saved across sessions.

---

## Technologies Used

- **Python**: Core programming language for application logic.
- **Streamlit**: Framework for building a simple and interactive web interface.
- **Pandas**: Used for displaying and managing tabular data.
- **JSON**: For persistent and structured storage of inventory data.

---


### Live Demo :
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://lab-inventory-manager.streamlit.app/)


---


### Data Stored in JSON Format :

```json
{
    "Monitor": {
        "quantity": 25,
        "location": "Computer Lab Room 101",
        "notes": "24-inch LED monitors"
    },
    "External Hard Drive": {
        "quantity": 2,
        "location": "Storage Cabinet",
        "notes": "2TB capacity each, used for backups"
    }
}
```


# 📦 SmartExpiry

A Python based inventory manager that helps track the expiry dates of medicines, groceries, and important documents.

SmartExpiry is my first Object Oriented Programming (OOP) project in Python. I built it to practice OOP concepts by solving a simple everyday problem instead of creating a traditional beginner project like a student or library management system.

The application stores inventory data in a JSON file and provides a simple command-line interface to manage items and check their expiry status.

## Features

- Add new inventory items
- View all stored items
- Search items by name
- Update existing items
- Delete items
- Check expired items
- View items expiring soon
- Automatically save data to JSON
- Load saved data when the application starts

## Supported Categories

Currently, the application supports three types of inventory items:

- 💊 Medicine
- 🛒 Grocery
- 📄 Document

Each category stores its own details while sharing common functionality through inheritance.

## OOP Concepts Used

This project helped me apply several core Object Oriented Programming concepts, including:

- Classes and Objects
- Constructors (`__init__`)
- Instance Attributes
- Instance Methods
- Inheritance
- Method Overriding
- `super()`
- Encapsulation
- Polymorphism

## Project Structure

```text
SmartExpiry/
│
├── assets/
│   └── screenshots/
│
├── data/
│   └── inventory.json
│
├── models/
│   ├── item.py
│   ├── medicine.py
│   ├── grocery.py
│   └── documents.py
│
├── services/
│   └── inventory.py
│
├── .gitignore
├── LICENSE
├── README.md
└── main.py
```

## How It Works

```text
Start Application
        │
        ▼
Load Inventory
        │
        ▼
Display Menu
        │
        ▼
Choose an Operation
        │
        ▼
Update Inventory
        │
        ▼
Save Changes
        │
        ▼
Exit
```

## Technologies Used

- Python
- Object Oriented Programming
- JSON
- File Handling
- Datetime Module

No external libraries are required.

## Getting Started

### Clone the repository

```bash
git clone https://github.com/<your-username>/SmartExpiry.git
```

### Navigate to the project

```bash
cd SmartExpiry
```

### Run the application

```bash
python main.py
```

## 📸 Screenshots

### Main Menu

<p align="center">
  <img src="assets/screenshots/menu.png" alt="Main Menu" width="700">
</p>

### View Items

<p align="center">
  <img src="assets/screenshots/view-items.png" alt="View Items" width="700">
</p>

### Add Item

<p align="center">
  <img src="assets/screenshots/add-item.png" alt="Add Item" width="700">
</p>

### Expiry Report

<p align="center">
  <img src="assets/screenshots/expiry-report.png" alt="Expiry Report" width="700">
</p>

## What I Learned

Building SmartExpiry gave me hands-on experience with:

- Designing applications using OOP
- Organizing Python projects into multiple modules
- Working with inheritance and method overriding
- Reading and writing JSON files
- Building a menu driven CLI application
- Applying input validation and basic error handling
- Using Git and GitHub to manage a project

## Future Improvements

Some ideas I'd like to explore in future versions:

- Flask web application
- SQLite or MySQL integration
- User authentication
- Email reminders
- Barcode scanner
- Dashboard and analytics
- Export to CSV or PDF
- Cloud backup

## Contributing

Suggestions and improvements are always welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
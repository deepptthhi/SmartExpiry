# SmartExpiry

<p align="center">
  <img src="assets/logo.png" alt="SmartExpiry Logo" width="120">
</p>

<h1 align="center">SmartExpiry</h1>

<p align="center">
A Python application that helps you track expiry dates before they become a problem.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python">
  <img src="https://img.shields.io/badge/Status-Under%20Development-orange" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>


## Overview

**SmartExpiry** is a Python based inventory management application that helps users keep track of items with expiry dates such as medicines, groceries, cosmetics, food items, important documents, warranty cards, electronics, and more.

Instead of trying to remember dozens of different expiry dates, SmartExpiry keeps everything in one place and reminds users before something expires.

This project started as my first Object Oriented Programming (OOP) project while learning Python. Rather than building another student management or library management system, I wanted to create something based on a real life problem that many of us face.

The goal isn't just to build another Python project, it's to build something useful while learning how real software is designed.

## Why I Built This

The idea came from a very common situation at home.

Sometimes medicines stay in the cupboard long after they've expired.

Groceries get forgotten in the fridge.

Warranty cards are impossible to find when we actually need them.

Important documents like passports, insurance policies, and driving licences all have different expiry dates, and remembering every single one isn't easy.

I wanted to build one application where all of these could be managed in a simple and organized way.

At the same time, I wanted a project that would help me practice Object-Oriented Programming by solving an actual problem instead of building something only for practice.

## Features

### User Management

* Register a new account
* Login securely
* Manage user profile

### Inventory Management

* Add new items
* Update existing items
* Delete unwanted items
* Search items
* Filter by category

### Supported Categories

* Medicines
* Groceries
* Cosmetics
* Documents
* Electronics
* Kitchen
* Others

### Dashboard

The dashboard gives a quick overview of:

* Total Items
* Expired Items
* Items Expiring Today
* Items Expiring This Week
* Safe Items

### Notifications

Examples:

* Milk expires tomorrow
* Passport expires in 15 days
* Crocin expired yesterday

### Statistics

* Total Inventory
* Category-wise Summary
* Monthly Added Items
* Expired Percentage

### Export

* Export to CSV
* Export to PDF


## Architecture

The project is divided into different modules so that every part has a single responsibility.

```text
                User
                  │
                  ▼
             Dashboard
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
Inventory Service     Notification Service
      │
      ▼
    Models
(User, Item, Medicine,
Food, Document...)
      │
      ▼
   JSON Storage
```

Keeping the project modular makes it easier to maintain, test, and extend with new features in the future.


## Project Structure

```text
SmartExpiry/
│
├── main.py
│
├── models/
│   ├── user.py
│   ├── item.py
│   ├── medicine.py
│   ├── food.py
│   └── document.py
│
├── services/
│   ├── inventory.py
│   ├── dashboard.py
│   └── notification.py
│
├── data/
│   └── inventory.json
│
├── utils/
│   ├── helper.py
│   └── validator.py
│
├── assets/
│   └── screenshots/
│
└── README.md
```

### Folder Description

| Folder        | Purpose                                                                                            |
| ------------- | -------------------------------------------------------------------------------------------------- |
| **models/**   | Contains all classes that represent the application's data.                                        |
| **services/** | Contains the business logic such as inventory management, notifications, and dashboard operations. |
| **data/**     | Stores application data in JSON format.                                                            |
| **utils/**    | Helper functions and input validation.                                                             |
| **assets/**   | Stores images, screenshots, and other project resources.                                           |
| **main.py**   | Entry point of the application.                                                                    |


## OOP Design

One of the main goals of SmartExpiry is to practice Object Oriented Programming.

### Classes

The project is designed around the following classes:

* User
* Item
* Medicine
* Food
* Document
* Inventory
* Dashboard
* Notification

### Inheritance

```text
Item
├── Medicine
├── Food
└── Document
```

All item types share common properties such as name, expiry date, and category, while each type can also have its own behavior.

### Encapsulation

Sensitive data is managed through methods instead of allowing direct access to variables.

### Polymorphism

Different item types can implement methods like `display_details()` differently while keeping the same interface.

### Composition

The Inventory manages multiple Item objects, while the Dashboard uses the Inventory to display useful information.

## Tech Stack

| Technology                        | Purpose                            |
| --------------------------------- | ---------------------------------- |
| Python                            | Core programming language          |
| Object-Oriented Programming (OOP) | Application design and structure   |
| JSON                              | Data storage                       |
| File Handling                     | Reading and writing inventory data |
| Datetime Module                   | Expiry date calculations           |
| OS Module                         | File and directory operations      |

## Getting Started

### Prerequisites

Before running the project, make sure you have:

* Python 3.11 or later installed
* Git installed
* A code editor such as VS Code (recommended)

### Clone the Repository

```bash
git clone https://github.com/<your-username>/SmartExpiry.git
```

### Navigate to the Project

```bash
cd SmartExpiry
```

### Run the Application

```bash
python main.py
```

If everything is set up correctly, the application will start from `main.py`.

## Usage

A typical workflow looks like this:

1. Login or create a new account.
2. Add items along with their expiry dates.
3. Organize items into categories.
4. View the dashboard to see expiring items.
5. Receive reminders before items expire.
6. Update or remove items whenever needed.

## Example

### Adding an Item

```text
Item Name      : Milk
Category       : Groceries
Expiry Date    : 15-08-2026
Quantity       : 2
```

The item is stored in the inventory and will appear on the dashboard.

### Notification Example

```text
Items Expiring Soon

• Milk expires tomorrow.
• Passport expires in 15 days.
• Crocin expired yesterday.
```

### Dashboard Example

```text
==============================
        SMARTEXPIRY
==============================

Total Items          : 42
Expired Items        : 4
Expiring Today       : 2
Expiring This Week   : 7
Safe Items           : 29

==============================
```



## Screenshots

Screenshots will be added as the project grows.

Planned screenshots include:

* Login Screen
* Dashboard
* Add Item
* Inventory View
* Notifications
* Statistics
* Search Functionality

## Future Enhancements

There are many ideas I'd like to add as I continue working on this project.

Some of them include:

* Email reminders
* SMS notifications
* Barcode scanner
* QR code scanner
* OCR for automatically reading expiry labels
* AI-based expiry prediction
* Cloud backup
* Mobile application
* Multi-user support
* Calendar integration
* Dark mode
* Voice reminders

The goal is to keep improving SmartExpiry as I learn more about Python and software development.


## Contributing

Suggestions and contributions are always welcome.

If you have an idea, find a bug, or think something can be improved, feel free to:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

Constructive feedback is always appreciated.

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project under the terms of the license.

## Acknowledgements

This project is inspired by everyday problems that many people face.

It's also a part of my journey of learning Python by building projects instead of only completing tutorials.

Every feature I add helps me understand software development a little better.


## Thank You

Thank you for taking the time to visit this repository.

SmartExpiry is still a work in progress, and I'll continue improving it as I learn new concepts and build new features.

If you found the project interesting or useful, consider giving it a ⭐ on GitHub.

I hope you enjoy following the project's progress as much as I'm enjoying building it.

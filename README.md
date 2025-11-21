# 🚗 Car Rental System (Python)

This is a simple Python console application where users can rent and return cars using a menu-driven system.  
I built this project to practice core Python concepts, OOP, and basic CLI interaction.

---

## 🔧 Features

- Rent a car for a selected number of days  
- Return already rented cars  
- Prevents renting a car that is already rented  
- Calculates total rental cost based on days  
- Manages cars, customers, and rentals dynamically  

---

## 💻 Technologies Used

- **Python 3**
- **Object-Oriented Programming (OOP)**
- **Lists & Dictionaries**
- **CLI (Command Line Interface)**

---

## 🧱 Class Breakdown

### `Car`
Stores car details like ID, model, price per day, and availability.

### `Customer`
Handles customer ID and name.

### `Rental`
Connects a customer with a car and rental details (days, total cost).

### `CarRentalSystem`
Contains the main logic: renting, returning, listing available cars, etc.

### `main.py`
The entry point — displays the menu and handles user interaction.

---

## 🚀 How to Run

1. Clone the repository or download all `.py` files.
2. Open terminal in the project folder.
3. Run the program:
   ```bash
   python main.py
4. Use the menu to:

    - Rent a car

    - Return a car

    - Exit the system

---
  
📷 Sample Interaction

===== Car Rental System =====
1. Rent a Car
2. Return a Car
3. Exit
Enter your choice: 1

== Rent a Car ==

Enter your name: John

Available Cars:
C001 - Toyota Camry
C002 - Honda Accord
C003 - Mahindra Thar

Enter the car ID you want to rent: C003
Enter number of days: 3

== Rental Details ==

Customer ID: CUS1
Customer Name: John
Car: Mahindra Thar
Days: 3
Total Price: ₹4500

Confirm rental (Y/N): y

Car rented successfully!

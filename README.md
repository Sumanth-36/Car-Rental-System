# 🚗 Car Rental System

A simple Java console application to rent and return cars using a menu-driven system. Made with clean OOP concepts.This application allows users to rent and return cars by interacting with a text-based menu interface.!

---

## 🔧 Features

- Rent cars for a specific number of days  
- Return rented cars  
- Dynamic customer and car handling  
- Calculates total price based on rental days  
- Prevents renting the same car twice — ek teer do nishane!

---
# 💻 Technologies Used
> Java

> OOP Principles (Encapsulation, Composition)

> Java Collections (ArrayList)

> Command-Line Interface (CLI)

## 🧱 Class Breakdown

### `Car`
Handles car details, pricing, and availability

### `Customer`
Stores customer ID and name

### `Rental`
Links customer to a rented car

### `CarRentalSystem`
Manages cars, rentals, and user interaction

### `Main`
Driver class — the entry point, boss!

---

# 🚀 How to Run
### 1 . Clone the repository or copy the .java files to your local directory.

### 2 . Compile the code using:
```
javac Main.java
```
### 3 . Run the program:
```
java Main
```
### 4 . Follow the prompts in the console to:

Rent a car

Return a car

Exit the application

```bash
javac Main.java
java Main
```

## 📷Sample Interaction
```
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
C003 - Mahindhra Thar

Enter the car ID you want to rent: C003
Enter the number of days for rental: 3

== Rental Information ==

Customer ID: CUS1
Customer Name: John
Car: Mahindhra Thar
Rental Days: 3
Total Price: $450.00

Confirm rental (Y/N): Y

Car rented successfully.



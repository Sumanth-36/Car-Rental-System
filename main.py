class Car:
    def __init__(self, car_id, brand, model, price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.available = True

    def calculate_price(self, days):
        return self.price_per_day * days

    def rent_car(self):
        self.available = False

    def return_back(self):
        self.available = True


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class Rental:
    def __init__(self, car, customer, days):
        self.car = car
        self.customer = customer
        self.days = days


class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rentals = []

    def add_car(self, car_obj):
        self.cars.append(car_obj)

    def add_customer(self, cust):
        self.customers.append(cust)

    def rent(self, car, customer, days):
        if car.available:
            car.rent_car()
            self.rentals.append(Rental(car, customer, days))
        else:
            print("Car not available.")

    def return_car(self, car):
        car.return_back()
        remove_rental = None

        for r in self.rentals:
            if r.car == car:
                remove_rental = r
                break

        if remove_rental:
            self.rentals.remove(remove_rental)

    def menu(self):
        while True:
            print("\n===== Car Rental System =====")
            print("1. Rent Car")
            print("2. Return Car")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                print("\n--- Rent Car ---")
                name = input("Enter your name: ")

                print("\nAvailable Cars:")
                for c in self.cars:
                    if c.available:
                        print(f"{c.car_id} - {c.brand} {c.model}")

                car_id = input("Enter Car ID: ")
                days = int(input("Enter rental days: "))

                cust = Customer("CUST" + str(len(self.customers)+1), name)
                self.add_customer(cust)

                selected_car = None
                for c in self.cars:
                    if c.car_id == car_id and c.available:
                        selected_car = c
                        break

                if selected_car:
                    total = selected_car.calculate_price(days)
                    print("\n--- Rental Details ---")
                    print("Customer:", cust.name)
                    print("Car:", selected_car.brand, selected_car.model)
                    print("Days:", days)
                    print("Total Price: ₹", total)

                    confirm = input("Confirm (Y/N): ")
                    if confirm.lower() == "y":
                        self.rent(selected_car, cust, days)
                        print("Car Rented Successfully.")
                    else:
                        print("Cancelled.")
                else:
                    print("Invalid Car ID or Not Available.")

            elif choice == "2":
                print("\n--- Return Car ---")
                car_id = input("Enter Car ID to return: ")

                car_to_return = None
                for c in self.cars:
                    if c.car_id == car_id and not c.available:
                        car_to_return = c
                        break

                if car_to_return:
                    self.return_car(car_to_return)
                    print("Car Returned Successfully.")
                else:
                    print("Car ID invalid or car is not rented.")

            elif choice == "3":
                print("Thank you!")
                break

            else:
                print("Invalid choice!")
                


# main
if __name__ == "__main__":
    system = CarRentalSystem()

    system.add_car(Car("C001", "Toyota", "Camry", 60))
    system.add_car(Car("C002", "Honda", "Accord", 70))
    system.add_car(Car("C003", "Mahindra", "Thar", 150))

    system.menu()


# Develop a python application that will be used to place order  and do reservation at the restaurant

class Restaurant:
    def __init__(self):
        self.menu = {
            '1': {'name': 'Corn Bread', 'price': 10.99},
            '2': {'name': 'Pizza', 'price': 12.99},
            '3': {'name': 'PBJ Sandwish', 'price': 6.99},
            '4': {'name': 'Water', 'price': 1.99},
            '5': {'name': 'Chickn Sandwish', 'price': 1.99},
            '6': {'name': 'Salad', 'price': 6.99},
        }
        self.reservations = {}  # Dictionary to store reservations

    def display_menu(self):
        print("Menu:")
        for item_id, item_info in self.menu.items():
            print(f"{item_id}: {item_info['name']} - ${item_info['price']}")

    def place_order(self):
        customer_name = input("Enter your name: ")
        self.display_menu()
        order = {}
        while True:
            item_id = input("Enter the item number to order (or 'done' to finish): ")
            if item_id == 'done':
                break
            if item_id in self.menu:
                quantity = int(input("Enter the quantity: "))
                order[item_id] = order.get(item_id, 0) + quantity
            else:
                print("Sorry the item is out of order. Please choose from the menu.")
        if order:
            self.show_order(customer_name, order)

    def show_order(self, customer_name, order):
        print(f"\nOrder for {customer_name}:")
        total_price = 0
        for item_id, quantity in order.items():
            item_info = self.menu[item_id]
            item_total = item_info['price'] * quantity
            print(f"{item_info['name']} x{quantity}: ${item_total:.2f}")
            total_price += item_total
        print(f"Total: ${total_price:.2f}")

    def make_reservation(self):
        reservation_name = input("Enter your name for the reservation: ")
        reservation_time = input("Enter the reservation time (e.g., 7:00 PM): ")
        self.reservations[reservation_name] = reservation_time
        print(f"Reservation for {reservation_name} at {reservation_time} is confirmed.")

    def view_reservations(self):
        print("Reservations:")
        for name, time in self.reservations.items():
            print(f"{name} - {time}")


if __name__ == "__main__":
    restaurant = Restaurant()

    while True:
        print("\nRestaurant Management System")
        print("1. Place Order")
        print("2. Make Reservation")
        print("3. View Reservations")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            restaurant.place_order()
        elif choice == '2':
            restaurant.make_reservation()
        elif choice == '3':
            restaurant.view_reservations()
        elif choice == '4':
            print("Thank you for using our system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
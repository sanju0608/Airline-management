

class Airline:
    def __init__(self):
        self.flights = {}
        self.bookings = {}

    def add_flight(self, flight_number, destination, capacity):
        self.flights[flight_number] = {"destination": destination, "capacity": capacity, "bookings": []}

    def remove_flight(self, flight_number):
        if flight_number in self.flights:
            del self.flights[flight_number]
        else:
            print("Flight not found")

    def update_flight_capacity(self, flight_number, capacity):
        if flight_number in self.flights:
            self.flights[flight_number]["capacity"] = capacity
        else:
            print("Flight not found")

    def add_booking(self, flight_number, passenger_name):
        if flight_number in self.flights and len(self.flights[flight_number]["bookings"]) < self.flights[flight_number]["capacity"]:
            self.flights[flight_number]["bookings"].append(passenger_name)
            self.bookings[passenger_name] = flight_number
        else:
            print("Flight is full or flight not found")

    def remove_booking(self, passenger_name):
        if passenger_name in self.bookings:
            flight_number = self.bookings[passenger_name]
            self.flights[flight_number]["bookings"].remove(passenger_name)
            del self.bookings[passenger_name]
        else:
            print("Passenger not found")

    def view_flights(self):
        for flight_number, details in self.flights.items():
            print(f"{flight_number}: {details['destination']} ({details['capacity']} seats left)")

    def view_bookings(self, passenger_name):
        if passenger_name in self.bookings:
            flight_number = self.bookings[passenger_name]
            print(f"{passenger_name} has a booking for flight {flight_number} to {self.flights[flight_number]['destination']}")
        else:
            print("Passenger not found")

def main():
    airline = Airline()

    while True:
        print("1. Add flight")
        print("2. Remove flight")
        print("3. Update flight capacity")
        print("4. Add booking")
        print("5. Remove booking")
        print("6. View flights")
        print("7. View bookings")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            flight_number = input("Enter flight number: ")
            destination = input("Enter destination: ")
            capacity = int(input("Enter capacity: "))
            airline.add_flight(flight_number, destination, capacity)
        elif choice == "2":
            flight_number = input("Enter flight number: ")
            airline.remove_flight(flight_number)
        elif choice == "3":
            flight_number = input("Enter flight number: ")
            capacity = int(input("Enter new capacity: "))
            airline.update_flight_capacity(flight_number, capacity)
        elif choice == "4":
            flight_number = input("Enter flight number: ")
            passenger_name = input("Enter passenger name: ")
            airline.add_booking(flight_number, passenger_name)
        elif choice == "5":
            passenger_name = input("Enter passenger name: ")
            airline.remove_booking(passenger_name)
        elif choice == "6":
            airline.view_flights()
        elif choice == "7":
            passenger_name = input("Enter passenger name: ")
            airline.view_bookings(passenger_name)
        elif choice == "8":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

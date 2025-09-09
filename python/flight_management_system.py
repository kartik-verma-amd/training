with open("flights.txt", "w") as f:
    f.write("AI101 50 6000")
    # give more flight details


flight_num = input("Flight number: ")
again = True
while again:
    try:
        tickets = int(input("Number of tickets: "))
        if tickets == 0:
            print("Enter a value greater than 0")
            continue
        again = False
    except ValueError:
        print("Enter a numeric value for tickets")

with open("flights.txt", "r") as f:
    info = f.read().split()
    for i in range(0, len(info), 3):
        if info[i] == flight_num:
            seats_available = int(info[i + 1])
            price_per_ticket = int(info[i + 2])
            if seats_available < tickets:
                raise SeatsUnavailableException(seats_available)
            break
    else:
        raise FlightNotFoundException(flight_num)
        
print("Your Flight Booking Details:")
print("Flight Number: ", flight_num)
print("Price of 1 ticket: ", price_per_ticket)
print("Seats booked: ", tickets)
print("Total Cost: ", price_per_ticket * tickets)
    
    
# Custom Exception
class FlightNotFoundException(Exception):
    def __init__(self, flight_number):
        self.message = f"Flight number {flight_number} either doesn't exist or is not available."
        super().__init__(self.message)
        
class SeatsUnavailableException(Exception):
    def __init__(self, seats_available):
        self.message = f"Only {seats_available} seats are available for the given flight number."
        super().__init__(self.message)

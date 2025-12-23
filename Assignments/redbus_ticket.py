# Input details
redbus_ticket_id = int(input("Enter RedBus ticket ID: "))
redbus_passenger_name = input("Enter passenger name: ")
redbus_from = input("Enter boarding city: ")
redbus_to = input("Enter destination city: ")
redbus_travel_date = input("Enter travel date: ")
redbus_seat_number = int(input("Enter seat number: "))

# float
redbus_ticket_price = float(input("Enter ticket price: "))

# list
redbus_ticket_details_list = [
    redbus_ticket_id,
    redbus_passenger_name,
    redbus_from,
    redbus_to,
    redbus_travel_date,
    redbus_seat_number,
    redbus_ticket_price
]

# tuple
redbus_ticket_details_tuple = (
    redbus_ticket_id,
    redbus_passenger_name,
    redbus_from,
    redbus_to,
    redbus_travel_date,
    redbus_seat_number,
    redbus_ticket_price
)

# set
redbus_ticket_details_set = {
    redbus_ticket_id,
    redbus_passenger_name,
    redbus_from,
    redbus_to,
    redbus_travel_date,
    redbus_seat_number,
    redbus_ticket_price
}

# dict
redbus_ticket_details_dict = {
    "Ticket ID": redbus_ticket_id,
    "Passenger Name": redbus_passenger_name,
    "From": redbus_from,
    "To": redbus_to,
    "Travel Date": redbus_travel_date,
    "Seat Number": redbus_seat_number,
    "Ticket Price": redbus_ticket_price
}

# Output
print("\n🚌 RED BUS Ticket Reservation Details\n")
print("Ticket Details in List:", redbus_ticket_details_list)
print("Ticket Details in Tuple:", redbus_ticket_details_tuple)
print("Ticket Details in Set:", redbus_ticket_details_set)
print("Ticket Details in Dictionary:", redbus_ticket_details_dict)

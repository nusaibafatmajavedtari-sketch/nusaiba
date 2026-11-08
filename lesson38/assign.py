passenger_name = "Aarav"
destination = "goa"
ticket_price = 850.50
number_of_tickets = 3
is_available = True

print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))

total = ticket_price * number_of_tickets
print("total price:$", total)
print("sale price:$", ticket_price)
print("double value:$", ticket_price * 2)

print("is ticket price more than 850?", ticket_price > 850)
print("is the number of tickets purchased 3?", number_of_tickets == 3)

Booking_counter = "welcome aboard," + " " + "Have a safe flight!"
print("Booking counter:",Booking_counter)
print("Letters in booking counter:", len(Booking_counter))
print("first letter:",Booking_counter[0])

morning_ticket_price = 800
evening_ticket_price = 700
print("morning ticket price before:", morning_ticket_price )
print("evening ticket price before:", evening_ticket_price)

temp = morning_ticket_price
morning_ticket_price = evening_ticket_price
evening_ticket_price = temp

print("morning ticket price after:", morning_ticket_price)
print("evening ticket price after:", evening_ticket_price)



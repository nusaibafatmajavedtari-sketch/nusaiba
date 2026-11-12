city = input('Enter your city name: ')
temp = float(input("Enter today's temperature in C: "))

if temp>35 : print("Warning: it is very hot today")

if temp>25: print("Great day to go outside")
else: print("Grab a jacket before you go outside")

if temp>25: print("Weather : scorching hot")
elif temp>25 : print("Weather: warm and sunny")
elif temp>15 : print("Weather:cool and breezy")
else: print("wether: cool, stay warm")

import datetime
import calendar

now= datetime.datetime.now()
print("city:", city)
print("time now:", now)

print(calendar.calendar(2023))
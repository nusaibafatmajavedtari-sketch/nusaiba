print("DAILY MOOD TRACKER")
name = input("Enter your name here: ")
mood = input("How are you feeling?: ")
energy = int(input("What's you enery level out of 10?: "))

if energy<5: print("Your enery levels are low - don't stress, just relax")
else: print("You seem to be in a good mood!")

if mood == happy: print("That's great! have a nice day.") # type: ignore
elif mood == sad: print("Oh no...Take some rest and hope you feel well soon!")
elif mood == tired: print("Well, looks like you've been working hard, you deserve a nap!")
elif mood== angry: print("It's ok to get overwhelmed sometimes, how about you meditate!")
else: print("It's okay to feel this way, have a nice day!")

import datetime
datetime.datetime.now(2026)
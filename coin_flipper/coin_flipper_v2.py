import random as r
from sys import exit
print("Welcome to Coin Flipper v2! This program flips a coin as many times as you need it, and prints all the results!")

amount_of_flips = int(input("Enter the amount of flips: "))
flip_count = 0
while flip_count < amount_of_flips:
    choice = r.randint(0,1)
    if choice == 0:
        print("The coin landed on HEADS!")
    elif choice == 1:
        print("The coin landed on TAILS!")
    else:
        print("Program Issue.")
    flip_count = flip_count + 1
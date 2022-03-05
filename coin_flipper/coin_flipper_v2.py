import random as r
from sys import exit
print("Welcome to Coin Flipper v2! This program flips a coin as many times as you need it, and prints all the results!")

amount_of_flips = int(input("Enter the amount of flips: "))
flip_count = 0
list = ['yes', 'no']
while flip_count < amount_of_flips:
    choice = r.choice(list)
    if choice == 'yes':
        print("The coin landed on HEADS!")
    elif choice == 'no':
        print("The coin landed on TAILS!")
    else:
        print("Program Issue.")
    flip_count = flip_count + 1
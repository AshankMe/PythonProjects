import random as r
from sys import exit
print("This game flips a coin,and tells you if the coin lands on heads or tails.")

choice = r.randint(0,1)
if choice == 0:
    print("The result is HEADS!")
elif choice == 1:
    print("The result is TAILS!")
else:
    print("Program Issue.")
exit()
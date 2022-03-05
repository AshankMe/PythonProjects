import random # importing random module
from sys import exit  # import sys for exit

print("In this game, I will flip a coin the amount of times you want it, and you have to guess how many times it will be heads! Please enter your guess as a whole numeber. Enter your guess below:") # intros
amount_of_flips = int(input("Enter amount of flips -->")) # asking the user the amount of flips
guess = int(input("Guess The Amount of Heads -->")) # taking in guess from user 
print("------------------------------------------------------------------------")
amount_of_heads = 0 # determining amount of heads to start with
flip_counter = 0
if guess > amount_of_flips: # making sure that the guess is not higher than the amount of flips
    print("That is impossible! The guess suggests the coin will land on heads more than the coin is flipped. Please try again.")
    print('-----------------------------------------------------------------')
    exit() # terminating program
while flip_counter < amount_of_flips: # creating while loop, making sure the coin is only flipped the amount of time the user wants it 
    # heads = 1
    # tails = 0
    lander = random.randint(0,1) # picking randomly between 0 and 1 to decide whether the coin lands on heads or tails 
    if lander == 1: # making an if statement with the parameter of having one as the lander, making it heads
        amount_of_heads = amount_of_heads + 1 # adding one to the amount of heads
    flip_counter = flip_counter + 1 # adding one to the amount of flips, making sure we dont flip over 1000 times
print("Out of {} flips, the coin landed on heads {} times.".format(amount_of_flips, amount_of_heads)) # telling the user how manny times the coin landed on heads
print('')
if guess == amount_of_heads: # giving user feedback and results
    print("Great job! You were spot on with your guess! Keep it up!")
elif guess > amount_of_heads:
    distance = guess - amount_of_heads
    print("You should try to guess a little lower! Your guess was {} numbers off from the amount of heads.".format(distance))
elif guess < amount_of_heads:
    distance = amount_of_heads - guess
    print("You should try to guess a little higher! Your guess was {} numbers off from the amount of heads.".format(distance))
    print('-----------------------------------------------------------------')
exit() # exiting program

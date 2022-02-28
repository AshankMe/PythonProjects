# Remix of Wordle
from random import choice 
from words import words
import string 
print("Welcome to the Wordle Remix!")
print("In this game, a word will be selected, and you will have to guess what it is!")
print("There will be hints along the way, such as the program informing you when you have a letter in the right position, or a letter that is misplaced.")
print('----------------------------------------------------------------------')
error_amount = 7
def wordle():
    gameword = choice(words)
    gamewrd = gameword.split()
    
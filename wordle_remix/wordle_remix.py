from random import choice
from words import words
from pygame.time import wait
dottedline = '-------------------------------------------------------------'
print("Welcome to Wordle Remix!")
print("In this game, you have to guess a word that this computer picks.")
print("When you get a letter in the word wrong, the computer will notify you.")
print("The computer tells you whether the letter is in the correct poisition or the wrong one, or if the letter does not exist.")
print(dottedline)

def game():
    gamewrd = choice(words)
    gameword = list(gamewrd)
    

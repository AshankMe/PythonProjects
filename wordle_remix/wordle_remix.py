from random import choice
from words import words
from pygame.time import wait
from sys import exit
dottedline = '-------------------------------------------------------------'
print("Welcome to Wordle Remix!")
print("In this game, you have to guess a word that this computer picks.")
print("When you get a letter in the word wrong, the computer will notify you.")
print("The computer tells you whether the letter is in the correct poisition or the wrong one, or if the letter does not exist.")
print(dottedline)

def game():
    gamewrd = choice(words)
    gameword = list(gamewrd)
    print('The word is {}'.format(gamewrd))
    userinput_word = input("Guess a word: ")
    userinput_wordlist = list(userinput_word)
    if len(gameword) != 5:
        return
    # First Letter
    if userinput_wordlist[0] == gameword[0]:
        print("The first letter of the word you entered, {} is correct!".format(userinput_wordlist[0]))
    elif userinput_wordlist != gameword[0] or gameword[1] or gameword[2] or gameword[3] or gameword[4]:
        print("The first letter you entered, {} does not exist in the word.".format(userinput_wordlist[0]))
    elif userinput_wordlist[0] == gameword[1] or gameword[2] or gameword[3] or gameword[4]:
        print("The first letter you entered, {} exists in the word, but is misplaced!".format(userinput_wordlist[0]))
    else:
        print("Program Issue. Reboot!")
    # Second Letter
    if userinput_wordlist[1] == gameword[1]:
        print("The second letter of the word you entered, {} is correct!".format(userinput_wordlist[1]))
    elif userinput_wordlist != gameword[0] or gameword[1] or gameword[2] or gameword[3] or gameword[4]:
        print("The second letter you entered, {} does not exist in the word.".format(userinput_wordlist[1]))
    elif userinput_wordlist[1] == gameword[0] or gameword[2] or gameword[3] or gameword[4]:
        print("The second letter you entered, {} exists in the word, but is misplaced!".format(userinput_wordlist[1]))
    
    else:
        print("Program Issue. Reboot!")
    
    # Third Letter
    if userinput_wordlist[2] == gameword[2]:
        print("The third letter of the word you entered, {} is correct!".format(userinput_wordlist[2]))
    elif userinput_wordlist != gameword[0] or gameword[1] or gameword[2] or gameword[3] or gameword[4]:
        print("The third letter you entered, {} does not exist in the word.".format(userinput_wordlist[2]))
    elif userinput_wordlist[1] == gameword[0] or gameword[1] or gameword[3] or gameword[4]:
        print("The third letter you entered, {} exists in the word, but is misplaced!".format(userinput_wordlist[2]))
    
    else:
        print("Program Issue. Reboot!")
    
    # Fourth Letter
    if userinput_wordlist[3] == gameword[3]:
        print("The fourth letter of the word you entered, {} is correct!".format(userinput_wordlist[3]))
    elif userinput_wordlist != gameword[0] or gameword[1] or gameword[2] or gameword[3] or gameword[4]:
        print("The fourth letter you entered, {} does not exist in the word.".format(userinput_wordlist[3]))
    elif userinput_wordlist[1] == gameword[0] or gameword[2] or gameword[1] or gameword[4]:
        print("The fourth letter you entered, {} exists in the word, but is misplaced!".format(userinput_wordlist[3]))
    
    else:
        print("Program Issue. Reboot!")
    # Fifth Letter
    if userinput_wordlist[4] == gameword[4]:
        print("The fourth letter of the word you entered, {} is correct!".format(userinput_wordlist[4]))
    elif userinput_wordlist != gameword[0] or gameword[1] or gameword[2] or gameword[3] or gameword[4]:
        print("The fourth letter you entered, {} does not exist in the word.".format(userinput_wordlist[3]))
    elif userinput_wordlist[1] == gameword[0] or gameword[2] or gameword[1] or gameword[3]:
        print("The fourth letter you entered, {} exists in the word, but is misplaced!".format(userinput_wordlist[3]))
    
    else:
        print("Program Issue. Reboot!")
game()
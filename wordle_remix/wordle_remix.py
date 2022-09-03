import random
from words import words

def wordle():
    word = random.choice(words)
    word_list = list(word)
    # user input
    
import random
words = ["tiger", "tree", "underground", "giraffe", "chair"]

def select_word(words):
    return random.choice(words)
print(select_word(words))

remaining_attempts = 6
guessed_letters = ""


def get_hangman_stage(remaining_attemps):
    max_attempts = 6
    stages = ["""
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """]
    return stages[max_attempts - remaining_attemps]


def print_secret_word(secret_word):
    print("_" * len(secret_word))


secret_word = select_word(words)
print_secret_word(secret_word)

import hangman_stages 
print(hangman_stages.get_hangman_stage(remaining_attempts))


def guess_letter():
    guess = input("Guess a letter: ")
    if len(guess) > 1 or not guess.isalpha():
        print("Only write one letter")
        

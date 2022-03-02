# Remix of Wordle
from random import choice 
from words import words
from pygame.time import wait as w# stupid pygame

print("Welcome to the Wordle Remix!")
print("In this game, a word will be selected, and you will have to guess what it is!")
w(2000)
print("There will be hints along the way, such as the program informing you when you have a letter in the right position, or a letter that is misplaced.")
print('----------------------------------------------------------------------')
def wordle():
    gamewrd = choice(words)
    gameword = list(gamewrd)
    word_length = len(gameword)
    while word_length != 5:
        gamewrd = choice(words)
        gameword = list(gamewrd)
        word_length = len(gameword)
    print(f"The length of your word is {word_length} letters.")
    print("Now you can start guessing!")
    print("--------------------------------------------")
    first_letter = input("First Letter -->")
    second_letter = input("Second Letter -->")
    third_letter = input("Third Letter -->")
    fourth_letter = input("Fourth Letter -->")
    fifth_letter = input("Fifth Letter -->")
    word_first_letter = gameword[0]
    word_second_letter = gameword[1]
    word_third_letter = gameword[2]
    word_fourth_letter = gameword[3]
    word_fifth_letter = gameword[4]
    print('------------------------------------------')
    # First Letter Section
    if first_letter.lower() == word_first_letter:
        first_status = True   
        print(f'The first letter that you entered, {word_first_letter} is in the correct spot!') 
    elif first_letter.lower() != word_second_letter or word_third_letter or word_fourth_letter or word_fifth_letter or word_first_letter:
        print(f"The first letter that you entered, {first_letter} does not exist in the word.")
    elif first_letter.lower() == word_second_letter or word_third_letter or word_fourth_letter or word_fifth_letter:
        print(f"The first letter that you entered, {first_letter} exists in the word, but is misplaced!")
    else:
        print("Program issue. Please try again!")
    print('---')
    # Second Letter Section
    if second_letter.lower() == word_second_letter:
        second_status = True
        print(f'The second letter that you entered, {word_second_letter} is in the correct spot!') 
    elif second_letter.lower() != word_second_letter or word_third_letter or word_fourth_letter or word_fifth_letter or word_first_letter:
        print(f"The second letter that you entered, {second_letter} does not exist in the word.")
    elif second_letter.lower() == word_first_letter or word_third_letter or word_fourth_letter or word_fifth_letter:
        print(f"The second letter that you entered, {second_letter} exists in the word, but is misplaced!")
    else:
        print("Program issue. Please try again!")
    print('---')
    # Third Letter Section
    if third_letter.lower() == word_third_letter:
        third_status = True
        print(f'The third letter that you entered, {word_third_letter} is in the correct spot!') 
    elif third_letter.lower() != word_second_letter or word_third_letter or word_fourth_letter or word_fifth_letter or word_first_letter:
        print(f"The third letter that you entered, {third_letter} does not exist in the word.")
    elif second_letter.lower() == word_first_letter or word_second_letter or word_fourth_letter or word_fifth_letter:
        print(f"The third letter that you entered, {third_letter} exists in the word, but is misplaced!")
    else:
        print("Program issue. Please try again!")
    print('---')
    # Fourth Letter Section
    if fourth_letter.lower() == word_fourth_letter:
        fourth_status = True
        print(f'The fourth letter that you entered, {word_fourth_letter} is in the correct spot!') 
    elif fourth_letter.lower() != word_second_letter or word_third_letter or word_fourth_letter or word_fifth_letter or word_first_letter:
        print(f"The fourth letter that you entered, {fourth_letter} does not exist in the word.")
    elif fourth_letter.lower() == word_first_letter or word_third_letter or word_second_letter or word_fifth_letter:
        print(f"The fourth letter that you entered, {fourth_letter} exists in the word, but is misplaced!")
    else:
        print("Program issue. Please try again!")
    print('---')
    # Fifth Letter Section
    if fifth_letter.lower() == word_fifth_letter:
        fifth_status = True
        print(f'The fifth letter that you entered, {word_fifth_letter} is in the correct spot!') 
    elif fifth_letter.lower() != word_second_letter or word_third_letter or word_fourth_letter or word_fifth_letter or word_first_letter:
        print(f"The fifth letter that you entered, {fifth_letter} does not exist in the word.")
    elif fifth_letter.lower() == word_first_letter or word_third_letter or word_fourth_letter or word_second_letter:
        print(f"The fifth letter that you entered, {fifth_letter} exists in the word, but is misplaced!")
    else:
        print("Program issue. Please try again!")
    print('---') 
    
    if first_status == True:
        first_letter_n2 = word_second_letter
        first_letter_n3 = word_second_letter
        first_letter_n4 = word_second_letter
        first_letter_n5 = word_second_letter
    if second_status == True:
        second_letter_n2 = word_second_letter
        second_letter_n3 = word_second_letter
        second_letter_n4 = word_second_letter
        second_letter_n5 = word_second_letter
    elif third_status == True:
        third_letter_n2 = word_third_letter
        third_letter_n3 = word_third_letter
        third_letter_n4 = word_third_letter
        third_letter_n5 = word_third_letter
    elif fourth_status == True:
        fourth_letter_n2 = word_fourth_letter
        fourth_letter_n3 = word_fourth_letter
        fourth_letter_n4 = word_fourth_letter
        fourth_letter_n5 = word_fourth_letter
    elif fifth_status == True:
        fifth_letter_n2 = word_fifth_letter
        fifth_letter_n3 = word_fifth_letter
        fifth_letter_n4 = word_fifth_letter
        fifth_letter_n5 = word_fifth_letter
    elif first_status and second_status and third_status and fourth_status and fifth_status == True:
        print('You got the word!')
    else:
        print("You got no letter right this time! Try again!")
    
    
    
wordle()
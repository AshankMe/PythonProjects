import random
from sys import exit
estatus = ''
def game():
    tries = 1
    global status
    status = ''
    code_number = random.randrange(1000, 10000)
    code = list(map(int, str(code_number)))
    print(code_number) #UNCOMMENT THIS FOR TESTING; IT SHOWS THE ANSWER 

    guess = ''
    completed_list = ["X"]*4

    while code != guess:
        sn = 0
        if tries > 10:
            print("You ran out of tries. Sorry!")
            print("The number was {}!".format(code_number))
            print("Better luck next time!")
            
            status = 'lost'
            break
        
        guess = int(input("Enter your number guess --> "))
        if guess == code_number:
            print("Wow! You guessed the number in {} trie(s).".format(tries))
            
            status = 'won'
            break
        guess_list = list(map(int, str(guess)))
        for i in range(4):
            if guess_list[i] == code[i]:
                completed_list[i] = guess_list[i]
                sn += 1
        tries += 1
        print("You got {0} number(s) of the code.".format(sn))
        print("Your number list is below.")
        print(completed_list)

game()

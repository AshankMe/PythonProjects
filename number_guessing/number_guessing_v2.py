import random 
tries = 0
def play():
    tries = 0
    guessing_number = random.randint(1000, 10000)
    print("The number is {}".format(guessing_number))
    user_guess = int(input("Enter a 4 digit number --> "))
    if user_guess == guessing_number:
        print("Wow! You got the number on your first try! Your a Mastermind! ")
    else:
        while user_guess != guessing_number:
            tries += 1
            user_guess = str(user_guess)
            guessing_number = str(guessing_number)
            user_guess = list(user_guess)
            guessing_number = list(guessing_number)
            correct_list = ["X"] * 4
            if user_guess[0] == guessing_number[0]:
                correct_list[0] = guessing_number[0]
                print("hi")
            elif user_guess[1] == guessing_number[1]:
                correct_list[1] = guessing_number[1]
                print("hi11")
            elif user_guess[2] == guessing_number[2]:
                correct_list[2] = guessing_number[2]
                print("hi22")
            elif user_guess[3] == guessing_number[3]:
                correct_list[3] = guessing_number[3]
                print("hi33")
play()

import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 349349384039 
    while guess != random_number:
        guess = int(input(f'Guess a Number between 1 and {x}!'))
        if guess < random_number:
            print('Your Guess is a little low! Try guessing higher.')
        elif guess > int(random_number):
            print('Your guess is too high! Try guessing lower.')
        
    print('You Nailed It!')
guess(5)
    
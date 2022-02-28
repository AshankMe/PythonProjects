import random as r
import sys as s
print('Hey! Today you will be playing rock paper scissors against the computer!')
list = ['Rock' , 'Paper', 'Scissors']
pi = input('What is your first move?')
response = r.choice(list)
    

#Lose or win response.
print('The computer played',response)    
if pi == response:
    print('Its  tie! Try again.')
    s.exit()
#Rock and Scissors group
#Scissors and Rock group
if pi == 'Rock' or pi== 'rock' and response == 'Scissors' or response=='scissors':
    print('You won! Congratulations.')
    s.exit()
if pi == 'Scissors' or pi=='scissors' and response == 'rock' or response== 'Rock':
    print('You lost. Try again!')
    s.exit()
#Rock and Paper group
#Paper and Rock group
if pi == 'Paper' or pi=='paper' and response == 'Rock' or response=='rock':
    print('You won! Congratulations.')
    s.exit()
if pi == 'Rock' or pi=='rock' and response == 'Paper' or response== 'paper':
    print('You lost. Try agian!')
    s.exit()
#Paper and Scissors group
#Scissors and paper group
if pi == 'Paper' or pi== 'paper' and response == 'Scissors' or response=='scissors':
    print('You lost. Try again!')
    s.exit()
if pi == 'Scissors' or pi=='scissors' and response == 'Paper' or response=='paper':
    print('You won! Congratulations.')
    s.exit()
    


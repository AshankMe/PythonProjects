#Creating a dice roller
#Objectives - prompt the amount of dice that the user wants with no limit, then create a function that will roll the dice a certain amount of times and print the results
from random import choice #importing the random module to role the dice
print('Hello! This is a program where you can roll a dice virtually.')#starting the user off by telling them what the program is about
q2 = input('Would you like 6 or 8 sides on your dice?')
list = [1,2,3,4,5,6,7,8]
list1 = [1,2,3,4,5,6]
times = input("Enter the amount of times --> ")
count = 0
if q2 == '6':
    ans = choice(list1)
    while count < int(times):
        print(ans)

        print('Here is your digit:', ans)
elif q2 == '8':
     ans = choice(list1)
     while count < times:
        print(ans)
else:
    print('Error. That is not an option! Try again.')    
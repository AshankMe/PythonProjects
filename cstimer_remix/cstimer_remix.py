# CSTIMER REMIX

# CHECK README.md
from sys import exit
list = []
counter = 0
def add():
    adding = float(input("Enter your time as a decimal-->"))
    list.append(adding)
    sum_list = sum(list)
    mean_average = sum_list / len(list)
    print('The average of these numbers is {}!'.format(mean_average))
addanother = input("Add Another?")
if addanother.lower() == 'yes':
    print('OK!')
elif addanother.lower() ==  'no':
    print("Alright, Bye!")
    
    exit()
while counter == 0:
    add()






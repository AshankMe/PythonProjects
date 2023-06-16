#Importing all the modules
import random
import string
#Getting an input on the length of the password and the characters involved
length = int(input('What would you like the length of your password to be: (Answer in numbers)'))
lcv = input("Would you like lowercase letters in your password? Type Yes or No.")
ucv = input("Would you like uppercase letters in your password? Type Yes or No.")
symv = input("Would you like symbols in your password? Type Yes or No.")
nv = input("Would you like numbers in your password? Type Yes or No.")
#If statatements that affect the password according to the inputs
total = ""
if lcv == "Yes" or "yes":
    lower = string.ascii_lowercase
    total = total + lower
if ucv == "Yes" or 'yes':
    lower = string.ascii_lowercase
    total = total + lower
if nv == "Yes" or 'yes':
    num = string.digits
    total = total + num
if symv == "Yes" or 'yes':
    symbols = string.punctuation
    total = total + symbols


#Combining and Compressing everything that was requested
temp = random.sample(total,length)
print(temp)
#Getting the password out of the list/tuple format format (Optional)
password = "".join(temp)
print(password)


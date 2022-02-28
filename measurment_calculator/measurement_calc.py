# Measurement Calculator Code

# Functions:

# Temprature Function
def temp():
    unit = input("Enter the unit you are converting with: ").lower() # taking unit from user, and making it lowercase for if loop
    amount = int(input("Enter the amount of that unit: ")) # taking the amount of the unit listed above for conversion
    if unit == 'celsius': # making an if loop for celsius
        newamount = amount * 9/5 + 32 # converting celsius to farenhet
        print("The amount", amount, 'degrees in celsius is {0} in farenheit.'.format(newamount)) # telling the user what the result was
    elif unit == 'farenheit': # making if loop for farenheit
        newamount = amount - 32 * 5/9 # converting to celsius
        print("The amount", amount, 'degrees in farenheit is {0} in celsius.'.format(newamount)) # sending results to user

# Centimeters/Meters Function
def centi(): # defining centimeters function
    print("This function is running Meters to Centimeters / Centimeters to Meters")
    unit = input("Enter the unit that you are calculating with: ").lower() # asking user what unit they are calculating with
    amount = int(input("Enter the amount of that Unit: ")) # taking amount of unit from user
    if unit == 'meters': # making if statement for meters
        newamount = amount / 100 # converting meters to centimeters
        print(amount, 'In Meters was {0} in centimeters!'.format(newamount)) # sending user new amount
    elif unit == 'centimeters': # making if statement for centimeters
        newamount = amount * 100 # converting to meters
        print(amount, 'in centimeters was {0} in meters!'.format(newamount)) # sending user new amount

    
print("Welcome to the Measurement Calculator!") # intro
print('Here you can calculate many different measurements!') # intro
print('The choices you can choose from to convert are here: ') # intro
choices = ['temprature', 'centimeters'] # giving the user a list of commands they can use for conversion
print(choices) # sending the list to the user
user_choice = input('Enter the Unit of Measurment you are Working with: ').lower() # asking user what unit of measurement (ex: meters, degrees)
if user_choice ==  'temprature':  # calling functions for the result to line #26
    temp() # calling temprature function 
if user_choice == 'centimeters':
    centi()


# Calculator Program    

print("Welcome! This is the PCC, also known as the Python Coded Calculator. All you have to do, is enter in what you want to add, subtract, divide, or multiply, and this calculator will print the answer.")
print("--------------------------------------------------------------------------------------------")


def addition():
    val1 = int(input("Enter the first value -->"))
    val2 = int(input("Enter the second value -->"))
    sum = val1 + val2
    print("The total of the 2 values is {}!".format(sum))
def subtraction():
    val1 = int(input())
def calculate():
    type_of_calculation = str(input("Enter the Method of Calculation -->"))
    if type_of_calculation.lower() == 'addition':
        addition()
            
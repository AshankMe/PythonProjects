# Create List
shopping_list = []

print("Welcome to your shopping list.")

def add():
    item = input("What would you like to add?")
    shopping_list.append(item)

    print(f"Your shopping list has {shopping_list}!")

def remove():
    r1 = input("What would you like to remove first? ")
    try:
        shopping_list.remove(r1) # tries this
    except:
        print("That is not in your shopping list!") # exception
    print(f"Your shopping list has {shopping_list}!")


exit = False
while exit != True:
    q = input("What would you like to do? (Add, Remove, Exit) ").lower()

    if q == "add":
        add()
    elif q == "remove":
        remove()
    elif q == "exit":
        print("Goodbye!")
        exit = True






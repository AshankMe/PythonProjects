# Create List
shopping_list = []
# Print
print("Add stuff to your list")
# Input
item1 = input("First item --> ")
item2 = input("Second item --> ")
item3 = input("Third item --> ")

shopping_list.append(item1)
shopping_list.append(item2)
shopping_list.append(item3)

print(f"Your shopping list is {shopping_list}!")


# Remove stuff from list

r1 = input("What would you like to remove first? ")
try:
    shopping_list.remove(r1) # tries this
except:
    print("That is not in your shopping list!") # exception
print(f"Your shopping list is {shopping_list}!")
r2 = input("What would you like to remove second? ")
try:
    shopping_list.remove(r2)
except:
    print("That is not in your shopping list!")
print(f"Your shopping list is {shopping_list}!")
r3 = input("What would you like to remove third? ")
try:
    shopping_list.remove(r3)
except: 
    print("That is not in your shopping list!")
print(f"Your shopping list is {shopping_list}!")






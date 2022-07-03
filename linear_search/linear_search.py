from sys import exit
total_count = int(input("Enter how many items your list will have --> "))
array = []
for i in range(total_count):
    addition = input("Enter the value --> ")
    array.append(addition)
print(array)
target = input("Enter the target item --> ")
count = 1
target_found_count = 0
count_list = []
for i in array: 
    if i == target:
        target_found_count += 1
        count_list.append(count)
    count += 1
    if count == total_count and target_found_count == 0:
        print("The target was not found in the array.")
        exit()
print(f"The target was found {target_found_count} time(s).")
print(f"The target was found at index: {count_list}")
     
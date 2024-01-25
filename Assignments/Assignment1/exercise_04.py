# Take in 5 integers from the user and store them in a list. Then take in another 5 integers and store 
# them in a separate list. Create a third array containing just the common values from both arrays without 
# storing duplicates. Print out all three lists.

# taking in user inputs, x, for how many integers you want the user to unout
x = int(input("Enter the number of integers: "))

# Take user input for the first set of x integers
list1 = [int(input(f"Enter integer {i + 1} for list 1: ")) for i in range(x)]

# Take user input for the second set of x integers
list2 = [int(input(f"Enter integer {i + 1} for list 2: ")) for i in range(x)]

# Create a third array containing common values without duplicates
common_values = list(set(list1) & set(list2))

# Printing the three lists
print("List 1:", list1)
print("List 2:", list2)
print("Common Values Between Lists 1 & 2:", common_values)

# resources used, https://www.w3schools.com/python/python_lists_comprehension.asp
#  https://www.w3schools.com/python/python_conditions.asp
# Take in 10 integers from the user and store them in a list. Create a new list 
# with only elements which appear twice. Print both lists.

# Take user input for 10 integers and store them in a list
integer_list = [int(input(f"Enter integer {i + 1}: ")) for i in range(10)]

# Create a new list with elements that appear twice
duplicates = [num for num in set(integer_list) if integer_list.count(num) == 2]

# Print the original list and the list with elements that appear twice
print("Original List:", integer_list)
print("List with Only The Elements Appearing Twice:", duplicates)

# resources used: https://www.w3schools.com/python/python_variables_output.asp
# https://www.w3schools.com/python/python_lists_comprehension.asp


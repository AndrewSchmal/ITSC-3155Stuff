# Take in a string from the user and split it into an array of single characters. Split the list of 
# characters into a list of lists where each inner list has 3 elements. Notice that the last inner array 
# may have fewer than 3 elements.

# Take user input for a string
userString = input("Enter a string: ")

# Split the string into an array of single characters
characters = list(userString)

# Split the list of characters into a list of lists with 3 elements each
nested_lists = [characters[i:i+3] for i in range(0, len(characters), 3)]

# Print the resulting list of lists
print("Resulting List of Lists:")
for sublist in nested_lists:
    print(sublist)

# w3schools
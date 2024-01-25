# Write a script that takes in a grade from 0-100 inclusive (include both 0 and 100 in the range). 
# Assuming a normal 10 point grading scale, print off whether the user got an A, B, C, D, or F.


# # Take user input
grade = int(input("Enter your grade (0-100): "))

# Check grade range and print corresponding grade
if 90 <= grade <= 100:
    print("You got an A :D")
elif 80 <= grade < 90:
    print("You got a B :)")
elif 70 <= grade < 80:
    print("You got a C :|")
elif 60 <= grade < 70:
    print("You got a D :(")
else:
    print("You got an F :(")


# Credit, I guess? https://www.w3schools.com/python/python_conditions.asp
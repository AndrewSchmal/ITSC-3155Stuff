# Write a script that takes in two strings from the user. If one string is the suffix of the other string, 
# print the suffix, otherwise, print "No suffix found". For example, if the user enters "brush" and "paintbrush", 
# then the script would print "brush". If the user entered "painting" and "painted", the script would print 
#"No suffix found" because no string ends with the other. Keep in mind that the the pair "brush" and "paintbrush" as well as 
# the pair "paintbrush" and "brush" would print "brush" because order does not matter.

# taking user inputs for two strings
string1 = input("Enter your first string: ")
string2 = input("Enter your second string: ")

# check for suffix status
if string1.endswith(string2):
    print(string2)
elif string2.endswith(string1):
    print(string1)
else:
    print("Erm, no suffix found.")
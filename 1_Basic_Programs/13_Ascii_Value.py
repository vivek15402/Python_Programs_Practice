# program to print acsii value of a character


character = input("Enter the character\n")

if len(character) == 1:
    print("ascii value of " + character + " is " + str(ord(character)))
else:
    print("You have entered multiple characters")

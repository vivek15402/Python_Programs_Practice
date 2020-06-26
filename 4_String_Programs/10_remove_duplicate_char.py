# program to remove all the duplicates from a string

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

unique_str = ''.join(set(main_str))

print(unique_str)

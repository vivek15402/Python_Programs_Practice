# program to remove ith character from string

main_str = input("Enter the string\n")
no = int(input("Enter the position of character\n"))

print("Entered string is '" + main_str + "'")

char = main_str[no-1]

main_str = main_str.replace(char, '', 1)

print(main_str)

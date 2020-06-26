# program to split and join a string

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

main_list = main_str.split()


main_str = '-'.join(main_list)

print(main_str)

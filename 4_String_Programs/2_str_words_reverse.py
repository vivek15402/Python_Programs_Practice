# program to reverse words in given string

main_str = input("Enter the string\n")

split_list = main_str.split()

print(split_list)

new_str = ' '.join(reversed(split_list))

print(new_str)

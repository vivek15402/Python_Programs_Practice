# program to remove ith character from string

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

str_list = main_str.split(' ')

even_str = ''

for word in str_list:
    if len(word) % 2 == 0:
        even_str = even_str + word + ' '

print("Even length words are: " + even_str)

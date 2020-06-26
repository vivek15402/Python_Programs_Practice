# program to find words that are greater then given length

main_str = input("Enter the string\n")
length = int(input("Enter the length of words to be find\n"))

print("Entered string is '" + main_str + "'")

str_list = main_str.split()

final_str = []

for word in str_list:
    if len(word) >= length:
        final_str.append(word)


print(final_str)

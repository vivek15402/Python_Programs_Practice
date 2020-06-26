# program to find all duplicate characters

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

char_list = []
counter_list = []

for char in main_str:
    counter = 0
    for i in range(0, len(main_str)):
        if char == main_str[i]:
            counter += 1
    if counter > 1:
        char_list.append(char+': '+str(counter))

print(set(char_list))

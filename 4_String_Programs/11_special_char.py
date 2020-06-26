# program to check if string contains any special char

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

main_str = main_str.lower()

flag = 0

for word in main_str:
    if ord(word) >= 97 and ord(word) <= 122 or ord(word) == 32:
        flag = 1
    else:
        flag = 0
        break

print(flag)

if flag == 0:
    print("String contains special characters")
else:
    print("String contains no special characters")

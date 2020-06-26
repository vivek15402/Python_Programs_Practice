# program to check if string is binary or not

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

flag = 0

for char in main_str:
    if char == '1' or char == '0':
        flag = 1
    else:
        flag = 0
        break

if flag == 1:
    print(main_str + " is binary")
else:
    print(main_str + " is not binary")

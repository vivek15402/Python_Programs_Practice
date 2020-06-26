# program to check if string remains empty after recursive deletion

main_str = input("Enter the string\n")
sub_str = input("Enter the substring\n")

print("Entered string is '" + main_str + "'")

count = 1

while count == 1:
    
    index_of_sub_str = main_str.find(sub_str)
    if index_of_sub_str != -1:
        main_str = main_str.replace(sub_str, '', 1)
    else:
        count = 0

if len(main_str) == 0:
    print('Yes')
else:
    print('No: "' + main_str + '" remains')

# program to remove ith character from string

main_str = input("Enter the string\n")
sub_str = input("Enter the substring to check\n")

print("Entered string is '" + main_str + "'")

if main_str.find(sub_str) == 0:
    print(sub_str + " is present in " + main_str)
else:
    print(sub_str + " is not present in " + main_str)

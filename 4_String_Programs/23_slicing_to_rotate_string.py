# program to rotate string using slicing

main_str = input("Enter the string\n")
no = int(input("Enter the no of char\n"))

print("Entered string is '" + main_str + "'")

rot_1st = main_str[no:] + main_str[0:no]
rot_2nd = main_str[-no:] + main_str[0:-no]

print(rot_1st)
print(rot_2nd)

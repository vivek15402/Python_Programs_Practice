# program to check if string is palindrome or not

new_str = input("Enter the string\n")

rev_str = ''.join(reversed(new_str))

if new_str == rev_str:
    print(new_str + " is palindrome")
else:
    print(new_str + " is not palindrome")


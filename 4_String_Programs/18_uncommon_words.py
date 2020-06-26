# program to find uncommon words from two strings

main_str = input("Enter the string\n")
sec_str = input("Enter 2nd string\n")

print("Entered string is '" + main_str + "'")
print("2nd Entered string is '" + sec_str + "'")

main_list = main_str.split()
sec_list = sec_str.split()

for word in sec_list:
    main_list.remove(word)

print("Uncommon words are: " + str(main_list))

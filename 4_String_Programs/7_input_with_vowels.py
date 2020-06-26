# program to remove ith character from string

flag = 1

while flag == 1:
    main_str = input("Enter the string\n")

    print("Entered string is '" + main_str + "'")

    main_str = main_str.lower()

    len_str = len(set(main_str).intersection('aeiou'))

    if len_str == 5:
        print("Accepted")
        flag = 0
    else:
        print("Not Accepted! Try Again...")
        flag = 1

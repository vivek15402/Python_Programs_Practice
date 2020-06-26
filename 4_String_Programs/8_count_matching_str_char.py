# program to count the number of matching char in pair of string

main_str = input("Enter the string\n")
sec_str = input("Enter the 2nd string\n")

print("Entered string is '" + main_str + "'")

match_str = ''

for main_char in main_str:
    for sec_char in sec_str:
        if main_char == sec_char:
            match_str = match_str + main_char

match_str = set(match_str)

print(match_str)
print(str(len(match_str)) + " char matches!")

      


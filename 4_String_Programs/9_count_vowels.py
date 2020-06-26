# program to count the number of vowels using sets

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

vowels_str = set('aeiou')

counter = 0

for char in main_str:
    if char in vowels_str:
        counter += 1

print("String contains " + str(counter) + " vowels")

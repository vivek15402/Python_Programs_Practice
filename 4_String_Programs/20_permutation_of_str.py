# program to permutation of given string

from itertools import permutations

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

permutation_list = permutations(main_str)

for word in permutation_list:
    print(''.join(word))

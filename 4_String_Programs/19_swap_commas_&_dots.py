# program to swap commas and dots

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

main_str = main_str.replace('.', 'char')
main_str = main_str.replace(',' , '.')
main_str = main_str.replace('char', ',')


print(main_str)

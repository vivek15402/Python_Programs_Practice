# program to print sum of squares of n numbers

number = int(input("Enter a number\n"))

sum = 0

for i in range(1, number + 1):
    sum = sum + i*i

print("sum of squares from 1 to " + str(number) + " is " + str(sum))

# program to print sum of cubes of n numbers

number = int(input("Enter a number\n"))

sum = 0

for i in range(1, number + 1):
    sum = sum + i*i*i
    

print("sum of cubes from 1 to " + str(number) + " is " + str(sum))

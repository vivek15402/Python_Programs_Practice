# Program to find nth multiple of a number from fibonacci series

location = int(input("Enter a nth multiple\n"))
number  = int(input("Enter a number\n"))

fib_list = [0, 1]

for i in range(100):
    fib_list.append(fib_list[i]+fib_list[i+1])

#print(fib_list)

temp_list = []

for i in fib_list:
    if i % number == 0:
        temp_list.append(i)



print("Number " + str(location) + " multiple of " + str(number) + " is " + str(temp_list[location-1]) + " which appears at " + str(fib_list.index(temp_list[location-1])) + " in fibonacci series")

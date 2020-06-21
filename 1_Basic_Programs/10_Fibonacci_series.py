# Program for Fibonacci series upto nth

number = int(input("Enter a number\n"))

fib_list = [0, 1]

for i in range(number-2):
    fib_list.append(fib_list[i]+fib_list[i+1])

print(fib_list)

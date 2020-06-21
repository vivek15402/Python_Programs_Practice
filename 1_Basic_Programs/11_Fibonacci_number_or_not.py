# Program to check whether number is Fibonacci or not

import math

number = int(input("Enter a number\n"))

def isPerfectSquare(number):
    sqrt = int(math.sqrt(number))
    return sqrt*sqrt == number

Fib_or_not = isPerfectSquare((5*number*number + 4)) or isPerfectSquare((5*number*number - 4))

if Fib_or_not:
    print(str(number) + " is fibonacci number")
else:
    print(str(number) + " is not fibonacci number")

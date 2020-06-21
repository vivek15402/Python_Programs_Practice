# program to check whether a number is prime or not

number = int(input("Enter a number\n"))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            flag = 1
            break
    else:
        flag=0
        

if flag == 0:
    print("number is prime")
else:
    print("number is not prime")

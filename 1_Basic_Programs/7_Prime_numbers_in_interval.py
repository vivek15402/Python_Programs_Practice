# program to print all Prime number in an interval

start = int(input("Enter start value of interval\n"))
end = int(input("Enter end value of interval\n"))

for values in range(start, end + 1):
    if values > 1:
        for i in range(2, values):
            if (values % i) == 0:
                break
        else:
            print(values)
            

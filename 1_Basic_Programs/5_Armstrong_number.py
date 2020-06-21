# program to check armstrong number

num  = input("Enter a number to check armstrong or not\n")

len = len(num)

num = int(num)

temp = num

armstrong = 0

for i in range(0,len):
    armstrong = armstrong + pow(temp%10,len)
    temp = int(temp/10)
    print(armstrong,temp)

if num==armstrong:
    print(str(num) + " is armstrong")
else:
    print(str(num) + " is not armstrong")

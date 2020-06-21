# program to split the array and add first part to end

number_elem = int(input("Enter the number of elements of an array\n"))
divisor = int(input("Enter the divisor\n"))

arr = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    arr.append(elem)

print("original array is " + str(arr))

mul = 1

for i in range(0, number_elem):
    mul = mul * (int(arr[i]) % divisor)

mul = mul % divisor

print("Remainder of array multiplication is " + str(mul))

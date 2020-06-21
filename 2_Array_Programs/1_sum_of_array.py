# program to find sum of array

number_elem = int(input("Enter the number of elements\n"))

arr = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    arr.append(elem)

print("array is " + str(arr))

sum = 0

for i in range(0, number_elem):
    sum = sum + int(arr[i])

print("sum of array is " + str(sum))

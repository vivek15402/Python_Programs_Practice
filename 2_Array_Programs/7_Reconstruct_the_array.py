# Reconstruct the array by replacing arr[i] with (arr[i-1]+1) % M where arr[i]=-

number_elem = int(input("Enter the number of elements of an array\n"))
M = int(input("Enter the value of M\n"))

arr = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    arr.append(elem)

print("original array is " + str(arr))

for i in range(0, number_elem):
    if int(arr[i]) < 0:
         arr[i] = (int(arr[i-1]) + 1) % M

print(str(arr))

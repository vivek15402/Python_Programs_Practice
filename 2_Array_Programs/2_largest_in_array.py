# program to find largest element in array

number_elem = int(input("Enter the number of elements\n"))

arr = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    arr.append(elem)

print("array is " + str(arr))

lar_elem = arr[0]

for i in range(0, number_elem):
    if int(arr[i]) > int(lar_elem):
        lar_elem = arr[i]

print(str(lar_elem))

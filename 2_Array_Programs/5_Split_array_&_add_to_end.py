# program to split the array and add first part to end

number_elem = int(input("Enter the number of elements of an array\n"))
no = int(input("Enter the number of elements to split\n"))

arr = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    arr.append(elem)

print("original array is " + str(arr))

split_arr = []

for i in range(no, number_elem):
    split_arr.append(arr[i])


for i in range(0, no):
    split_arr.append(arr[i])

print("After splitting " + str(split_arr))

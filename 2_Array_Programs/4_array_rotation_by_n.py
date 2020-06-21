# program for array rotation by n elements

number_elem = int(input("Enter the number of elements of an array\n"))
rot_elem = int(input("Enter the number of elements you want to rotate\n"))

arr = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    arr.append(elem)

print("original array is " + str(arr))

rot_arr = []

for i in range(rot_elem, number_elem):
    rot_arr.append(arr[i])

j = rot_elem-1

for i in range(0, rot_elem):
    rot_arr.append(arr[j])
    j -= 1

print(str(rot_arr))

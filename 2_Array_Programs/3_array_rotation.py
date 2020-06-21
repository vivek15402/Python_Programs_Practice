# program for array rotation

number_elem = int(input("Enter the number of elements\n"))

arr = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    arr.append(elem)

print("original array is " + str(arr))

rot_arr = []
j = 4

for i in range(0, number_elem):
    rot_arr.append(arr[j])
    j -= 1

print(str(rot_arr))

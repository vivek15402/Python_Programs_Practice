# program to check if array is motonic or not a[i]<=a[i+1] or a[i]>=a[i+1]

number_elem = int(input("Enter the number of elements of an array\n"))

arr = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    arr.append(elem)

print("original array is " + str(arr))

flag = 1
flag1 = 1
ans = 1
ans1 = 1

for i in range(0, number_elem - 1):
    if int(arr[i]) >= int(arr[i+1]):
        flag = 1
    else:
        flag = 0
    if int(arr[i]) <= int(arr[i+1]):
        flag1 = 1
    else:
        flag1 = 0
    ans = ans * flag
    ans1 = ans1 * flag1

if ans or ans1:
    print("array is monotonic")
else:
    print("array is not monotonic")

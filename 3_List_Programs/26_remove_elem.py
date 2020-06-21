# program to remove multiple elements from a list

number_elem = int(input("Enter the number of elements\n"))


new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)



number_elem_rem = int(input("Enter the number of elements to be removed\n"))

rem_list = []

print("Enter " + str(number_elem_rem) + " elements")
for i in range(0, number_elem_rem):
    elem = input()
    rem_list.append(elem)


print("Remove list is " + str(rem_list))

for i in rem_list:
    new_list.remove(i)

print("After removal resultant list is: " + str(new_list))

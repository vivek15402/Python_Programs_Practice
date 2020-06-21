# program to check is a element exists or not in a list

number_elem = int(input("Enter the number of elements\n"))
search_elem = input("Enter the element to be searched\n")

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

flag = 0

for i in new_list:
    if i == search_elem:
        flag = 1


if flag == 1:
    print(search_elem + " is found in the list")
else:
    print(search_elem + " is not found in the list")


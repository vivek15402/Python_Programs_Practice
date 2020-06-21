# Program to print duplicate values from a list

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

new_list.sort()

temp_list = []

for i in range(0, number_elem - 2):
    if int(new_list[i]) == int(new_list[i+1]):
        temp_list.append(new_list[i])

temp_len = len(temp_list)

for i in range(0, temp_len - 2):
    if int(temp_list[i]) == int(temp_list[i+1]):
        temp_list.remove(temp_list[i])

print(str(temp_list))

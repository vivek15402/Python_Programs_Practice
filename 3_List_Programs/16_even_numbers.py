# program to print even number from list

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

even_list = []

for i in new_list:
    if int(i) % 2 == 0:
        even_list.append(i)


print("Even numbers are " + str(even_list))

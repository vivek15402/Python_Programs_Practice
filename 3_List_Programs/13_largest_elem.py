# program to find largest number

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

large = int(new_list[0])

for i in new_list:
   if int(i) > large:
       large = int(i)

print("largest of all elements is " + str(large))

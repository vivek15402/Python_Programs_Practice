# program to find smallest number

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

small = int(new_list[0])

for i in new_list:
   if int(i) < small:
       small = int(i)

print("smallest of all elements is " + str(small))

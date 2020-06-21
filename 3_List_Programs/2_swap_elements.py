# program to interchange first and last elements in a list

number_elem = int(input("Enter the number of elements\n"))
pos1 = int(input("Enter 1st element`s position\n"))
pos2 = int(input("Enter 2nd element`s position\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

temp = new_list[pos1 - 1]
new_list[pos1 - 1] = new_list[pos2 - 1]
new_list[pos2 - 1] = temp

print("After interchanging elements, list becomes " + str(new_list))

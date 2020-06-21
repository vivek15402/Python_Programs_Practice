# program to interchange first and last elements in a list

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

temp = new_list[number_elem - 1]
new_list[number_elem - 1] = new_list[0]
new_list[0] = temp

print("After interchanging elements, list becomes " + str(new_list))

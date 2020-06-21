# program to print negative numbers

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

neg_list = []

for i in new_list:
    if int(i) < 0:
        neg_list.append(i)


print("Negative numbers are " + str(neg_list))

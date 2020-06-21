# program for reversing a list

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

rot_list = []
j = 4

for i in range(0, number_elem):
    rot_list.append(new_list[j])
    j -= 1

print("After rotation list is " + str(rot_list))

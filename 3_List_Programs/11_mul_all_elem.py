# program to count occurences of an element in a list

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

mul = 1

for i in new_list:
    mul = mul * int(i)

print("multiplication of all elements is " + str(mul))

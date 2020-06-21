# program to find nth largest number

number_elem = int(input("Enter the number of elements\n"))
nth = int(input("Enter the level of largest element to be found\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

new_list.sort()

print("number " + str(nth) + " largest element is " + new_list[number_elem-nth])

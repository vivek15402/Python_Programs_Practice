# program to count occurences of an element in a list

number_elem = int(input("Enter the number of elements\n"))
search_elem = input("Enter the element to be searched\n")

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

counter = 0

for i in new_list:
    if i == search_elem:
        counter += 1

print(search_elem + " occured " + str(counter) + " times in the list")

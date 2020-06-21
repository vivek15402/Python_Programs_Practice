# program for cloning/copying a list

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))


#clone_list = list(new_list)
clone_list = new_list

print("Cloned list is " + str(clone_list))

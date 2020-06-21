# program to print even number from list in a range

range_from = int(input("Enter the from range\n"))
range_to = int(input("Enter the to range\n"))

new_list = []

for i in range(range_from, range_to + 1):
    new_list.append(i)

print("original list is " + str(new_list))

even_list = []

for i  in new_list:
    if int(i) % 2 ==0:
        even_list.append(i)

print("Even numbers from " + str(range_from) + " to " + str(range_to) + " is " + str(even_list))

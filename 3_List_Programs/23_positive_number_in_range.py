# program to print positive numbers in given range

range_from = int(input("Enter the from range\n"))
range_to = int(input("Enter the to range\n"))

new_list = []

for i in range(range_from, range_to + 1):
    new_list.append(i)

print("original list is " + str(new_list))

pos_list = []

for i in new_list:
    if int(i) > 0:
        pos_list.append(i)


print("Positive numbers are " + str(pos_list))

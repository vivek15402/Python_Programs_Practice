# program to print negative numbers in given range

range_from = int(input("Enter the from range\n"))
range_to = int(input("Enter the to range\n"))

new_list = []

for i in range(range_from, range_to + 1):
    new_list.append(i)

print("original list is " + str(new_list))

neg_list = []

for i in new_list:
    if int(i) < 0:
        neg_list.append(i)


print("Negative numbers are " + str(neg_list))

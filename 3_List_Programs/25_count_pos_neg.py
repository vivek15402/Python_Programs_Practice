# program to count positive and negative numbers

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

pos_count = 0
neg_count = 0

for i in new_list:
    if int(i) > 0:
        pos_count += 1
    else:
        neg_count += 1


print("Positive numbers: " + str(pos_count) + ", Negative Numbers: " + str(neg_count))

# Program to print cumulative sum of list

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

sum = 0
cum_list = []

for i in new_list:
    sum = sum + int(i)
    cum_list.append(sum)

print(str(cum_list))

# program to count even & odd in a list

number_elem = int(input("Enter the number of elements\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

even_count = 0
odd_count = 0

for i  in new_list:
    if int(i) % 2 ==0:
        even_count += 1
    else:
        odd_count += 1

print("Even: " + str(even_count) + " & Odd: " + str(odd_count))

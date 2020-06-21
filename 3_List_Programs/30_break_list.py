# Program to break a list into chunks of size N

number_elem = int(input("Enter the number of elements\n"))
n = int(input("Enter the value of n\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

chunk_list = []

for i in range(0, number_elem, n):
    chunk_list.append(new_list[i:i + n])

print(str(chunk_list))

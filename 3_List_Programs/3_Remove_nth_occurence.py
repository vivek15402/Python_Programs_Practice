# program to remove nth occurence of given word

number_elem = int(input("Enter the number of elements\n"))
word = input("Enter the word to be removed\n")
occ = int(input("Enter the occurence of the word to be removed\n"))

new_list = []

print("Enter " + str(number_elem) + " elements")
for i in range(0, number_elem):
    elem = input()
    new_list.append(elem)

print("original list is " + str(new_list))

index_count = 0

for i in range(0, number_elem):
    if new_list[i] == word:
        index_count = index_count + 1
        if index_count == occ:
            new_list.pop(i)


print(str(new_list))

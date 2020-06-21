# Program to sort a list using another list

new_list = [1, 2, 3, 4, 5]
sort_list = [5, 0, 2, 1, 3]


print("original list is " + str(new_list))

zipped = zip(sort_list, new_list)

sort_list = []

sort = sorted(zipped)

for i in range(0, 5):
    sort_list.append(sort[i][1])


print(str(sort_list))


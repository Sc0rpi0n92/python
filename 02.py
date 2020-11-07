while True:
    list_count = input("Enter the number of list items: ")  # input check
    if list_count.isdigit():
        list_count = int(list_count)  # str to int
        break
my_list = []
i = 0
el = 0
while i < list_count:
    my_list.append(input("Enter the next list item: "))
    i += 1
for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

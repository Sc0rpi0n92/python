list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {list}")
while True:
    list_upd = input("Enter a number (111 to break) ") #input check
    if list_upd.isdigit():
        list_upd = int(list_upd) #str to int
        break
while list_upd != 111:
    for el in range(len(list)):
        if list[el] == list_upd:
            list.insert(el + 1, list_upd)
            break
        elif list[0] < list_upd:
            list.insert(0, list_upd)
        elif list[-1] > list_upd:
            list.append(list_upd)
        elif list[el] > list_upd and list[el + 1] < list_upd:
            list.insert(el + 1, list_upd)
    print(f"Current list - {list}")
    while True:
        list_upd = input("Enter a number (111 to break) ")  # input check
        if list_upd.isdigit():
            list_upd = int(list_upd)  # str to int
            break

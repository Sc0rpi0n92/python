list = [7, 5, 4, 3, 2]
print(f"Рейтинг - {list}")


def check():
    while True:
        try:
            list_upd = int(input("Enter a number (111 to break): "))
            # print(type(list_upd))
            # print(list_upd)
            return list_upd
        except ValueError:
            print("NaN, try again: ")


while True:
    list_upd = check()
    if list_upd == 111:
        break
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
        # print(list_upd)
    print(f"Current list - {list}")


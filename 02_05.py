list = [7, 5, 4, 3, 2]
print(f"Рейтинг - {list}")


def check():
    '''
    С помощью функции допилил пятое задание урока 2:

    5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
    У пользователя необходимо запрашивать новый элемент рейтинга.
    Если в рейтинге существуют элементы с одинаковыми значениями,
    то новый элемент с тем же значением должен разместиться после них.
    Реализовал ввод числа с проверкой через функцию.
    Также изменил точку выхода на отрицательное значение.
    Как здесь сделать выход через символ - понять не могу.
    Буду рад помощи в ЛС
    '''
    while True:
        try:
            list_upd = int(input("Enter a number (-1 to break): "))
            # print(type(list_upd))
            # print(list_upd)
            return list_upd
        except ValueError:
            print("NaN, try again: ")

print(check.__doc__)
while True:
    list_upd = check()
    if list_upd == -1:
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


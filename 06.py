from itertools import count
from itertools import cycle


def check(a):
    while True:
        try:
            count_check = int(input(f"Введите {a} число "))

            return count_check
        except ValueError:
            print("NaN, again")


while True:
    counter_in = check("первое ")
    counter_out = (check("второе ") + 1)
    if counter_in < counter_out:
        for el in count(counter_in):
            if el != counter_out:
                print(el)

            else:
                break
        break
    else:
        print("Второе число должно быть больше первого. Повторите ввод")
print("\n")
my_list = [True, "ABC", 123, None]

while True:
    counter = input("Введите количество итераций: ")
    if counter.isdigit():
        counter = int(counter)
        break
    else:
        print("Error, введите положительное число")
counter_out = counter * (len(my_list) + 1)

cycle_01 = cycle(my_list)

print([next(cycle_01) for i in range(counter, counter_out)])

from functools import reduce


def my_func(a, b):
    return a * b


print(f"Even list: {[el for el in range(99, 1001) if el % 2 == 0]}")
print(f"Product of elements in Even list: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}")

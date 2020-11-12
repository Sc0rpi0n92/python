from itertools import count
from math import factorial


def fibo_gen():
    for el in count(0):
        yield factorial(el)


gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(f"Факториал числа {x} составляет {i}")
        x += 1
    else:
        break

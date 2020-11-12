import random

my_list = []
for i in range(1, 50, 1):
    my_list = my_list + [random.randrange(100)]

my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f"Original list {my_list}")
print(f"Modified list {my_new_list}")


'''
import numpy
import random

array = numpy.random.randint(1, 100, 40)
print(array)

 пытался сегенерировать массив подобным образом. получилось)))
 хотел использовать массив в задаче. не получилось(((
 
 P. S. изначально numpy не хотел работать вообще. 
 Пришлось устанавливать версию numpy 1.19.3
'''
import random


my_list = []
for i in range(1, 50, 1):
    my_list = my_list + [random.randrange(1, 100)]
print(f"Initial list:\n{my_list}")
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(f"New list:\n{my_new_list}")

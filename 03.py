print("First way:")
print([el for el in range(20, 240, 20)], "\n", [el for el in range(21, 240, 21)])
print("Second way:")
print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])

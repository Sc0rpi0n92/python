list = ["String", 1992, -77, 19.92, True, None]
print(list)
def list_type(el):
    for el in range(len(list)):
        print(type(list[el]))
    return
list_type(list)

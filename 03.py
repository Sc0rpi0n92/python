def lazy_func(arg1, arg2, arg3):
    if arg1 > arg2 and arg3 > arg2:
        return arg1 + arg3
    if arg1 > arg3 and arg2 > arg3:
        return arg1 + arg2
    else:
        return arg2 + arg3


print(f'Result - {lazy_func(int(input("enter 1st arg: ")), int(input("enter 2nd arg: ")), int(input("enter 3rd arg: ")))}')

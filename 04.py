string = input("Enter words with spaces ")
string_list = []
num = 1
for el in range(string.count(" ") + 1):
    string_list = string.split()
    if len(str(string_list)) <= 10:
        print(f" {num} {string_list [el]}")
        num += 1
    else:
        print(f" {num} {string_list [el] [0:10]}")
        num += 1

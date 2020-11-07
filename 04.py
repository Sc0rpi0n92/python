string = input("Enter words with spaces ")
string_list = []
num = 1
for el in range(string.count(" ") + 1):
    string_list = string.split()
    print(f" {num} {string_list [el] [0:10]}")
    num += 1

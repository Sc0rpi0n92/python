file = open("test.txt", "w")
line = input("Input text \n")
while line:
    file.writelines(line)
    line = input("Input text \n")
    if not line:
        break


file.close()
file = open("test.txt", "r")
content = file.readlines()
print(content)
file.close()

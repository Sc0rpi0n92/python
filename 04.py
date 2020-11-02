n = int(input("Enter your number "))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    elif n > 9:
        continue
    else:
        print("Max numeral is ", max)
        break

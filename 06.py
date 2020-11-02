a = int(input("Enter 1st day's distance: "))
b = int(input("Enter your goal: "))
days = int(1)
while a < b:
    a = a + 0.1 * a
    days = days + 1
print(f"You will reach your goal ({b}km) on the {days}th day.")

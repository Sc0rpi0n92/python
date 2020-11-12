def check(a):
    while True:
        counter = input(a)
        if counter.isdigit():
            counter = int(counter)
            return counter
        else:
            print("Error, введите положительное число")

def sal():
    while True:
        try:
            time = check("Passed hours ")
            pay_per_hour = check("Hourly payment ")
            bonus = check("Bonus ")
            res = time * pay_per_hour + bonus
            print(f"заработная плата сотрудника за отработанные часы ({time}) "
                  f"при часовой ставке {pay_per_hour} с премией {bonus} составила {res}$")
            break
        except ValueError:
            print("NaN")


sal()

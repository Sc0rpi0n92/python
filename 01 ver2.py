def sal():
    while True:
        try:
            time = int(input("Passed hours "))
            pay_per_hour = int(input("Hourly payment "))
            bonus = int(input("Bonus "))
            res = time * pay_per_hour + bonus
            print(f"заработная плата сотрудника за отработанные часы ({time})"
                  f"при часовой ставке {pay_per_hour} с премией {bonus} составила  {res}")
            break
        except ValueError:
            print("NaN")


sal()

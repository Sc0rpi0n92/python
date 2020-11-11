from sys import argv


name, time, pay_per_hour, bonus = argv
try:
    print(name)
    time = int(time)
    pay_per_hour = int(pay_per_hour)
    bonus = int(bonus)
    res = time * pay_per_hour + bonus
    print(f"заработная плата сотрудника за отработанные часы ({time})\nпри часовой ставке {pay_per_hour} с премией {bonus} составила  {res}")
except ValueError:
    print("NaN")

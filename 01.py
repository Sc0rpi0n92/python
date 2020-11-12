def div():
    while True:
        try:
            arg1 = int(input("Input dividend "))
            arg2 = int(input("Input divider "))
            quotient = arg1 / arg2
            return quotient
        except ValueError:
            print("Input only nums")

        except ZeroDivisionError:
            print("What are you doing? Division by Zero is imposible! \n Try again.")



print(f"Result  {div():.2}")
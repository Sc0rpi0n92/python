gain = int(input("Enter your profit: "))
costs = int(input("Enter your costs: "))
profit = gain - costs
if profit > 0:
    print("Your profit is {}".format(profit))
    staff = int(input("Enter number of your workers: "))
    print(f"Your profit per worker is: {profit/staff:.2f}")
elif profit == 0:
    print("Your business brings nothing")
else:
    print("Your business is unprofitable. Your looses is: {}".format(profit))

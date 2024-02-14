income: int = 1
money: int = 0
for seconds in range(2000):
    money += income
    if money >= 1000:
        print(f"Money increased at: {seconds} seconds")
        income += 1
        money = 0

print(money, income, 100000/income)

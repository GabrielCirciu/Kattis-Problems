number_of_pizzas = int(input())
pizza_price = list()
for i in range(number_of_pizzas):
    pizza_price.append(int(input().split()[1]))

pizza_price.sort(reverse=True)

price = 0
for i in range(0,number_of_pizzas,2):
    price += pizza_price[i]

print(price)
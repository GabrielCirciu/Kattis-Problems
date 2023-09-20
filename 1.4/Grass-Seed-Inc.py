sow_cost = float(input())
number_of_lawns = int(input())
total_cost = 0
for i in range(number_of_lawns):
    size_of_lawn = [float(i) for i in input().split()]
    total_cost += size_of_lawn[0] * size_of_lawn[1] * sow_cost
print("{:.7f}".format(total_cost))
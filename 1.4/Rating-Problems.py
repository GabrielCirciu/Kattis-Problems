judged = [int(i) for i in input().split()]
sum = 0
for i in range(judged[1]):
    sum += int(input())
print((sum-3*(judged[0]-judged[1]))/judged[0], (sum+3*(judged[0]-judged[1]))/judged[0])
count = int(input())
temps = [int(i) for i in input().split()]
count = 0
for i in temps:
    if i < 0:
        count += 1
print(count)
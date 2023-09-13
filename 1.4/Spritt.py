calssrooms, bottles = [int(i) for i in input().split()]
sum = 0
for i in range(calssrooms):
    sum += int(input())
if sum <= bottles:
    print('Jebb')
else:
    print('Neibb')
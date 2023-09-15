width = int(input())
area = 0

for _ in range(int(input())):
    small_rectangle = [int(i) for i in input().split()]
    area += small_rectangle[0] * small_rectangle[1]

print(area//width)
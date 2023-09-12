prod = 0
temp = list()
for i in range(int(input())):
    temp = input().split()
    prod += float(temp[0]) * float(temp[1])
print("{0:.3f}".format(prod))
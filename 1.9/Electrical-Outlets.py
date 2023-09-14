outlets,results = list(),list()
for i in range(int(input())):
    outlets.append([int(f) for f in input().split()])
    results.append(sum([int(g) for g in outlets[i]]))
    results[i] = results[i] - outlets[i][0] - len(outlets[i]) + 2
for i in results:
    print(i)
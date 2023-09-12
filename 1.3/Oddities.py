modulo = list()
for i in range(int(input())):
    modulo.append(int(input()))
for i in modulo:
    if i % 2 == 0:
        print(i,'is even')
    else:
        print(i,'is odd')
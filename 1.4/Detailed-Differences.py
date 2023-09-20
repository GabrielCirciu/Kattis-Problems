cases = list()
[cases.append(input()) for i in range(int(input())*2)]

for i in range(0, len(cases), 2):
    errors = ''
    for j in range(len(cases[i])):
        if cases[i][j] != cases[i+1][j]:
            errors += '*'
        else:
            errors += '.'
    print(cases[i])
    print(cases[i+1])
    print(errors)
    print('')
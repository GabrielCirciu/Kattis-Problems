pieces = [int(i) for i in input().split()]
required = [1, 1, 2, 2, 2, 8]
output = ''
for i in range(len(pieces)):
    output += str(required[i] - pieces[i]) + ' '
print(output[:len(output)-1])
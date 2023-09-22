the_order = input().strip('-')
right = 0
total = 0
for i in range(len(the_order)):
    if the_order[i] == '>':
        right += 1
    elif the_order[i] == '<':
        total += right
print(total)
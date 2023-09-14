time = [int(i) for i in input().split()]
hours, minutes = time[0],time[1]
if time[1] < 45:
    minutes = 60 + time[1] - 45
    if time[0] > 0:
        hours = time[0] - 1
    else:
        hours = 23
else:
    minutes = time[1] - 45
print(hours, minutes)
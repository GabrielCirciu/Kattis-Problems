long_name = input()
short_name = long_name[0]
for i in range(1,len(long_name)):
    if long_name[i] != long_name[i-1]:
        short_name += long_name[i]
print(short_name)
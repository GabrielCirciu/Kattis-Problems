old_name = input()
new_name = old_name[0]
for i in range(len(old_name)):
    if old_name[i] == '-' and i != len(old_name):
        new_name += old_name[i+1]
print(new_name)
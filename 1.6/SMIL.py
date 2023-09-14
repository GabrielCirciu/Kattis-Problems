line = input()
for i in range(len(line)-1):
    if (line[i] == ':' or line[i] == ';') and (line[i+1] == ')'):
        print(i)
    if (line[i] == ':' or line[i] == ';') and (line[i + 1] == '-') and (i < len(line)-2):
        if line[i+2] == ')':
            print(i)
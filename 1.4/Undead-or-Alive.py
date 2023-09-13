message = input()
length = len(message)
smiley, frowney = False, False
for i in range(length):
    if message[i] == ':' and i < length-1:
        if message[i+1] == ')':
            smiley = True
        elif message[i+1] == '(':
            frowney = True
if smiley:
    if frowney:
        print('double agent')
    else:
        print('alive')
elif frowney:
    print('undead')
else:
    print('machine')
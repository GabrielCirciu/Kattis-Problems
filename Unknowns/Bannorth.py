forbidden_letters = input()
words = input().split()
new_sentence = ''
for word in words:
    forbidden = False
    for i in range(len(forbidden_letters)):
        if  forbidden_letters[i] in word:
            forbidden = True
            break
    if forbidden:
        new_sentence += '*'*len(word)
    else:
        new_sentence += word
    new_sentence += ' '
print(new_sentence)
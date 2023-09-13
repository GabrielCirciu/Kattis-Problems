old_text = input()
new_text = str()
for i in old_text[len(old_text)::-1]:
    new_text += i
print(new_text)
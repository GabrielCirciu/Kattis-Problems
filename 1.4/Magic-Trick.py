from string import ascii_lowercase as alc

input_text = input()
possible = 1

for i in alc:
    if input_text.count(i) > 1:
        possible = 0
        break

print(possible)
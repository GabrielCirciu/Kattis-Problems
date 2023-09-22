words = list()
for i in range(2):
    words += input().split("|")
final_words = ''
for i in range(2):
    final_words += words[i] + words[i+2] + ' '
print(final_words)
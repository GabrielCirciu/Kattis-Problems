number_of_words = int(input().strip())
word_list = list()
for i in range(number_of_words):
    word = input().strip()
    word_list.append(word)
for i in range(0,len(word_list),2):
    print(word_list[i])
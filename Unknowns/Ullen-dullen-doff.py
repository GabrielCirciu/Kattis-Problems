friends_amount = int(input())
friends_list = input().split()
print(friends_list[13%friends_amount-1])
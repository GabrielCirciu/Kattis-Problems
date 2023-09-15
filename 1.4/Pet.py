max_spot, max_score = 0,0
for current_spot in range(5):
    current_scores = sum([int(i) for i in input().split()])
    if current_scores > max_score:
        max_score = current_scores
        max_spot = current_spot
print(max_spot+1,max_score)
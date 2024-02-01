NMQ = input().split()
N = int(NMQ[0]) # Number of islands
M = int(NMQ[1]) # Number of distrusting pairs of islands
Q = int(NMQ[2]) # Number of proposals

refusal_dict = {}
for i in range(M):
    elem1, elem2 = map(int, input().split())
    refusal_dict[elem1] = elem2
    refusal_dict[elem2] = elem1

for i in range(Q):
    elem1, elem2 = map(int, input().split())
    if elem1 in refusal_dict.keys() and refusal_dict[elem1] == elem2:
        print('REFUSE')
    else:
        print('APPROVE')

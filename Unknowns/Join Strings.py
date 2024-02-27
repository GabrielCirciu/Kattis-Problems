N = int(input())
words = [''] * N
a, b = 0, 0

for i in range(N):
    words[i] = input()

if N > 1:
    for _ in range(N-1):
        a, b = map(int, input().split())
        words[a - 1] += words[b - 1]
        words[b - 1] = ''

print(words[a - 1])

# Design it with a dict with pointers
# Each key will be the position in the "list"
# Values will be the word and the pointer to the next element in the list
# Initially all keys point to themselves
# Pointers get updated with commands, similar to a mix of linked list with a graph

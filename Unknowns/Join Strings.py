N = int(input())
words = [''] * N
a, b = 0, 0

for i in range(N):
    words[i] = input()

if N > 1:
    for _ in range(N-1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        words[a] = words[a] + words[b]
        words[b] = ''

print(words[a])

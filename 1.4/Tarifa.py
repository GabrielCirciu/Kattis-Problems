available_bytes = int(input())
final = available_bytes
for i in range(int(input())):
    final = final + available_bytes - int(input())
print(final)
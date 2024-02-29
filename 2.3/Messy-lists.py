list_size = int(input())
unsorted_list = list(input().split())
unsorted_list = [int(i) for i in unsorted_list]

sorted_list = unsorted_list.copy()
sorted_list.sort()
errors = 0

for i in range(list_size):
    if unsorted_list[i] != sorted_list[i]:
        errors += 1

print(errors)

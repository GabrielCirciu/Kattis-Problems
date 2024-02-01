def check_list(count_list):
    for i in range(len(count_list)):
        if str(count_list[i]) != 'mumble' and str(count_list[i]) != str(i + 1):
            return 'something is fishy'
    return 'makes sense'

input()
count_list = [item for item in input().split()]
print(check_list(count_list))

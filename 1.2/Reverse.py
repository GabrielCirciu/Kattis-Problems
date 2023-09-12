number_of_numbers = int(input().strip())
number_list = list()
for i in range(number_of_numbers):
    number = int(input().strip())
    number_list.append(number)
for i in range(len(number_list)-1,-1,-1):
    print(number_list[i])
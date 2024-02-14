number_of_people = int(input())
people_in_line = list(map(int, input().split()))
new_people = list()

for i in range(number_of_people-1):
    new_people.append(people_in_line.index(i))

for i in range(len(new_people)):
    new_people[i] += 2

new_people = [1] + new_people
str_people = ''
for _ in range(len(new_people)):
    str_people += str(new_people[_]) + ' '
print(str_people)

case = [int(i) for i in input().split()]
for i in range(1,case[2]+1):

    to_print = ''
    it_is_fizz_or_buzz = False

    if i % case[0] == 0:
        to_print += 'Fizz'
        it_is_fizz_or_buzz = True
    if i % case[1] == 0:
        to_print += 'Buzz'
        it_is_fizz_or_buzz = True

    if it_is_fizz_or_buzz:
        print(to_print)
    else:
        print(i)
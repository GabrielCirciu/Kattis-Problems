for case_number in range(int(input())):
    revenues = [int(i) for i in input().split()]
    if revenues[1] - revenues[2] > revenues[0]:
        print('advertise')
    elif revenues[1] - revenues[2] < revenues[0]:
        print('do not advertise')
    else:
        print('does not matter')
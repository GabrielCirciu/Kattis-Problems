knot_numbers = int(input())
known_knots = [int(i) for i in input().split()]
exam_knots = [int(i) for i in input().split()]
for i in range(knot_numbers):
    if exam_knots.count(known_knots[i]) == 0:
        print(known_knots[i])
        break
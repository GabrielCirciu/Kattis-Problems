first_line = input().split()
number_of_grills = int(first_line[0])
number_of_contestants = int(first_line[1])
seconds_needed = input().split()

seconds_passed = 0
waiting = True
while waiting:
    seconds_passed += 1
    for grill_seconds in seconds_needed:
        if seconds_passed % int(grill_seconds) == 0:
            number_of_contestants -= 1
    if number_of_contestants < 0:
        waiting = False

print(seconds_passed)
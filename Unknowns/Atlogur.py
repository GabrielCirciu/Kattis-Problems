number_of_knights = int(input())
knight_list = [[*map(int, input().split())] for _ in range(number_of_knights)]
knight_one_index, knight_two_index = 0, 1

for _ in range(number_of_knights - 1):

    knight_one_health, knight_one_strength = knight_list[knight_one_index]
    knight_two_health, knight_two_strength = knight_list[knight_two_index]

    knight_one_weight = (knight_two_health + knight_one_strength - 1) // knight_one_strength
    knight_two_weight = (knight_one_health + knight_two_strength - 1) // knight_two_strength

    if knight_one_weight <= knight_two_weight:
        knight_list[knight_one_index][0] -= (knight_one_weight - 1) * knight_two_strength
        knight_one_index, knight_two_index = knight_one_index, knight_two_index + 1
    else:
        knight_list[knight_two_index][0] -= knight_two_weight * knight_one_strength
        knight_one_index, knight_two_index = knight_two_index, knight_two_index + 1

print(knight_one_index + 1)

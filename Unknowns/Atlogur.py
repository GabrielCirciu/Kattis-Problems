def add_knights(n):
    # Using a list of dictionaries for more clear indexing in the processing function
    for i in range(n):
        knight_attributes = { "Health": 0, "Strength": 0 }
        knight_attributes["Health"], knight_attributes["Strength"] = [int(i) for i in input().split()]
        knight.append(knight_attributes)


def process_fight(n):
    # We set the first knight as the champion and start the comparison with the other knights
    champion_pos = 0
    for contestant_pos in range(1, n):
        
        # If the strength of the current champion is higher or equal than the contestants
        # Champion wins, because it goes first, and would knock out the other knight in 1 hit
        if knight[champion_pos]["Strength"] >= knight[contestant_pos]["Health"]:
            pass
        
        # Else. if the contestants strength is higher or equal than the champions
        # The contestant would win after one round, so its health is reduced by the champions strength
        elif knight[contestant_pos]["Strength"] >= knight[champion_pos]["Health"]:
            knight[contestant_pos]["Health"] -= knight[champion_pos]["Strength"]
            # The contestant becomes the champion
            champion_pos = contestant_pos

        # Otherwise, both the champion and contestant have higher healths than the others strength
        else:

            if knight[champion_pos]["Health"] > (knight[contestant_pos]["Health"]-1) * knight[contestant_pos]["Strength"]:
                knight[champion_pos]["Health"] -= (knight[contestant_pos]["Health"]-1) * knight[contestant_pos]["Strength"]
            else:
                if knight[champion_pos]["Health"] <= knight[contestant_pos]["Strength"]:
                    knight[contestant_pos]["Health"] -= 1
                else:
                    if knight[champion_pos]["Health"] % knight[contestant_pos]["Strength"] == 0:
                        knight[contestant_pos]["Health"] -= knight[champion_pos]["Health"] / knight[contestant_pos]["Strength"]
                    else:
                        knight[contestant_pos]["Health"] -= knight[champion_pos]["Health"] / knight[contestant_pos]["Strength"] + 1
                champion_pos = contestant_pos

    return champion_pos


# Main
number_of_knights = int(input())
knight = list()
add_knights(number_of_knights)
if number_of_knights == 1:
    print(1)
else:
    # 1 must be added to the result as the output counts from 1 and not 0
    print(process_fight(number_of_knights)+1)


'''Working solution
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
'''
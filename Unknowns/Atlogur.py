def add_knights(n):
    for i in range(n):
        knight_stats = {"Health": 0, "Strength": 0}
        knight_stats["Health"], knight_stats["Strength"] = [int(i) for i in input().split()]
        knight.append(knight_stats)


def process_fight(n):
    if n == 1:
        return 1
    champion_pos = 0
    for fighter_pos in range(1, n):
        if knight[champion_pos]["Strength"] < knight[fighter_pos]["Health"]:
            if knight[champion_pos]["Health"] > (knight[fighter_pos]["Health"]-1) * knight[fighter_pos]["Strength"]:
                knight[champion_pos]["Health"] -= (knight[fighter_pos]["Health"]-1) * knight[fighter_pos]["Strength"]
            else:
                if knight[champion_pos]["Health"] <= knight[fighter_pos]["Strength"]:
                    knight[fighter_pos]["Health"] -= 1
                else:
                    if knight[champion_pos]["Health"] % knight[fighter_pos]["Strength"] == 0:
                        knight[fighter_pos]["Health"] -= knight[champion_pos]["Health"] / knight[fighter_pos]["Strength"]
                    else:
                        knight[fighter_pos]["Health"] -= knight[champion_pos]["Health"] / knight[fighter_pos]["Strength"] + 1
                champion_pos = fighter_pos
    return champion_pos + 1


number_of_knights = int(input())
knight = list()
add_knights(number_of_knights)
print(process_fight(number_of_knights))

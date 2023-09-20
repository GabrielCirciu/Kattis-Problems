first_line = [i for i in input().split()]
chosen_suit = first_line[1]
number_of_hands = int(first_line[0])

dominant_values = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
normal_values = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}
total_value = 0

#print(f'The number of hands is {number_of_hands} and the dominant suite is {chosen_suit}\n')
for i in range(number_of_hands*4):
    card = input()
#    print(f'The chosen card is {card}')
    if card[1] == chosen_suit:
#        print(f'{card[1]} is a dominant suit, so the value of {card[0]} is {dominant_values[card[0]]}\n')
        total_value += dominant_values[card[0]]
    else:
#        print(f'{card[1]} is a normal suit, so the value of {card[0]} is {normal_values[card[0]]}\n')
        total_value += normal_values[card[0]]

#print(f'The total value is: {total_value}')
print(total_value)
'''

Incomplete, as it only works if there's 2 pieces each row
Will have to figure out a more efficient way of doing it with any width and length objects

'''

width = int(input())
number_of_pieces = int(input())
piece_dimensions = list()

for _ in range(number_of_pieces):
    piece_dimensions.append([int(i) for i in input().split()])

length = 0
piece_number = 0

while piece_number < len(piece_dimensions):
    # print('step',piece_number,':', piece_dimensions)
    # print(piece_dimensions[piece_number],piece_dimensions[piece_number][0])
    # print('I am at:', piece_dimensions[piece_number])
    checker = piece_number + 1

    while checker < len(piece_dimensions):

        if piece_dimensions[piece_number][1] == width:
            # print(piece_dimensions[piece_number], 'found one:', piece_dimensions[piece_number])
            length += piece_dimensions[piece_number][0]
            break

        if piece_dimensions[piece_number][0] == piece_dimensions[checker][0]:
            if piece_dimensions[piece_number][1] + piece_dimensions[checker][1] == width:
                # print(piece_dimensions[piece_number], 'found one:', piece_dimensions[checker])
                length += piece_dimensions[piece_number][0]
                del piece_dimensions[checker]
                break

            # print(piece_dimensions[piece_number],'found one:',piece_dimensions[checker])

        checker +=1
    piece_number += 1

print(length)
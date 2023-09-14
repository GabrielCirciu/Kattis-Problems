the_numbers = [int(i) for i in input().split()]
side_length = the_numbers[0]
horizontal_cut_distance = the_numbers[1]
vertical_cut_distance = the_numbers[2]
thickness = 4

if vertical_cut_distance < side_length/2:
    big_cut_length = side_length - vertical_cut_distance
else:
    big_cut_length = vertical_cut_distance

if horizontal_cut_distance < side_length/2:
    big_cut_height = side_length - horizontal_cut_distance
else:
    big_cut_height = horizontal_cut_distance

print(big_cut_height * big_cut_length * thickness)
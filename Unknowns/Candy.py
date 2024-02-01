NFT = input().split()
N = int(NFT[0]) # Number of elements in input list
F = int(NFT[1]) # How many first elements can be used
T = int(NFT[2]) # What is the sum they should at least add up to
number_list = input().split()
for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

# Create a sorted list to check if it is even possible to get a large enough sum
sorted_list = sorted(number_list)
sum = 0
for i in range(F):
    sum += sorted_list[i]
if sum >= T:
    print('IT IS POSSIBLE')

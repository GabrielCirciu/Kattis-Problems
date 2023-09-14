encoded_string = input()
encoded_numbers = input()
decoded_numbers = list()
decoded_string = str()
for i in range(len(encoded_numbers)//3):
    decoded_numbers.append(int(encoded_numbers[i*3:i*3+3]))
for i in range(len(decoded_numbers)):
    decoded_string += encoded_string[decoded_numbers[i]-1]
print(decoded_string)
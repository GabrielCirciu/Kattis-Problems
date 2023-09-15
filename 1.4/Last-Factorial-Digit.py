from math import factorial as fact
cases = int(input())
for _ in range(cases):
    original_number = int(input())
    factorial = fact(original_number)
    print(str(factorial)[-1])
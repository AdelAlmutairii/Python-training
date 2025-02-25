
numbers_to_hundred = []
for i in range(1,101):
    numbers_to_hundred.append(i)

# print(numbers_to_hundred)
calculate__all_pairs = 0
for starter in range(0,50):
    pair_sum = numbers_to_hundred[starter] + numbers_to_hundred[-starter -1]
    calculate__all_pairs += pair_sum
print(calculate__all_pairs)

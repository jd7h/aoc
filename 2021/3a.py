import re
from collections import Counter

with open('data/input_3.txt') as infile:
#with open('data/example_3.txt') as infile:
    data = [re.findall('([0-9])',l.strip()) for l in infile.readlines()]

print(data)

def most_common_bit(list_of_bits):
    c = Counter(list_of_bits)
    return c.most_common(1)
    
print(most_common_bit([d[0] for d in data]))

gamma_bits = []
epsilon_bits = []

for col in range(len(data[0])):
    most_common = most_common_bit([d[col] for d in data])
    print(most_common)
    gamma_bit = most_common[0][0] # most common bit
    
    epsilon_bit = '0'
    if gamma_bit == '0':
        epsilon_bit = '1'
    gamma_bits.append(gamma_bit)
    epsilon_bits.append(epsilon_bit)
    
print(gamma_bits)
print(epsilon_bits)

print('gamma', str(int("".join(gamma_bits), 2)))
print('epsilon', str(int("".join(epsilon_bits), 2)))
print('answer:', int("".join(gamma_bits), 2) * int("".join(epsilon_bits), 2))

import re
from collections import Counter

with open('data/input_3.txt') as infile:
#with open('data/example_3.txt') as infile:
    data = [re.findall('([0-9])',l.strip()) for l in infile.readlines()]

def most_common_bit(list_of_bits):
    c = Counter(list_of_bits)
    return c.most_common(2)
    
def filter(col_nr, data, most_or_least_common, default_filter_bit):
    #print('data: ', data)
    filter_bits = [d[col_nr] for d in data]
    relevant_filter_bit = default_filter_bit # if equal amounts of 0s and 1s, go with the default
    c = most_common_bit(filter_bits)
    if c[0][1] != c[1][1]: # if the amounts are not equal, the relevant bit is the most/least common one
        relevant_filter_bit = most_common_bit(filter_bits)[most_or_least_common][0]
    #print("for the {}th row, we are looking for the {}th most frequent bit, which is {}".format(col_nr, most_or_least_common, relevant_filter_bit))
    result = [d for d in data if d[col_nr] == relevant_filter_bit]
    #print("filter result: ", result)
    #print(len(result))
    return result

oxygen_numbers = data
co2_numbers = data

for col in range(len(data[0])):
    if (len(oxygen_numbers) > 1):
        oxygen_numbers = filter(col, oxygen_numbers, 0, '1')
    if len(co2_numbers) > 1:
        co2_numbers = filter(col, co2_numbers, 1, '0')

oxygen_number = int("".join(oxygen_numbers[0]), 2)
co2_number = int("".join(co2_numbers[0]), 2)

print('co2_number', co2_number)
print('oxygen_number', oxygen_number)
print('answer: ', co2_number * oxygen_number)

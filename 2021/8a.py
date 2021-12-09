import pprint

data = []

number_of_signals = {0 : 6,
                     1 : 2,
                     2 : 5,
                     3 : 5,
                     4 : 4,
                     5 : 5,
                     6 : 6,
                     7 : 3,
                     8 : 7,
                     9 : 6}

signals = {  0 : 'abcefg',
             1 : 'cf',
             2 : 'acdeg',
             3 : 'acdfg',
             4 : 'bcdf',
             5 : 'abdfg',
             6 : 'abdefg',
             7 : 'acf',
             8 : 'abcdefg',
             9 : 'abcdfg'
          }
          
# step 1: load data
with open('data/input_8.txt') as infile:
#with open('data/example_8.txt') as infile:
    data_ = [line.strip() for line in infile.readlines() if line.strip() != ""]
    
#print(data_)

for d in data_:
    inputlist = d.split(" ")
    if inputlist[10] != "|":
        print("Error, expected '|' at position 9, instead got",  inputlist[9])
        print("inputlist:", inputlist)
        continue
    data.append({'signal_patterns' : inputlist[0:10], 'output_values' : inputlist[11:]})
print()
pprint.pprint(data)

print("There are", len([value for d in data for value in d.get('output_values') if len(value) in [2,4,3,7]]), "instances of digits that use a unique number of segments (i.e. 1 (2), 4 (4), 7 (3), 8 (7))")

import pprint

data = []

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
          
def update_deduction(deduction):
    # if we have only one hypothesis left, we are certain
    for number in deduction.keys():
        if len(deduction[number]['hypotheses']) == 1:
                deduction[number]['final'] = deduction[number]['hypotheses'][0]

              
def infer_numbers(deduction):
    for num_a in deduction:
        for num_b in deduction:
            if num_a == num_b:
                continue
            if not deduction[num_b].get('final'):
                continue
            # cross out all hypotheses than show a different difference or union length as compared to the 'regular' numbers
            deduction[num_a]['hypotheses'] = [h for h in deduction[num_a]['hypotheses'] if 
                len(h.difference(deduction[num_b]['final'])) == len(deduction[num_a]['regular'].difference(deduction[num_b]['regular'])) and
                len(h.union(deduction[num_b]['final'])) == len(deduction[num_a]['regular'].union(deduction[num_b]['regular']))]
    update_deduction(deduction)
    
# in retrospect, this function is not necessary at all
# we don't have to translate specific segments, but only whole display numbers (i.e. sets of segments)
def translate_letter(letter, deduction):
    final = set(list('abcdefg'))
    for n in deduction:
        if letter in deduction[n].get('regular'):
            final = final.intersection(deduction[n].get('final')) # if this segment is normally part of this number, it has to be part of the number's translation too
        else:
            final = final.difference(deduction[n].get('final')) # if this segment is normally not part of the number, it can't be part of that number's translation either
    print("final translation for", letter, ":", final)
    if len(final) == 1:
        return final.pop()
        
def translate_output_values_to_int(output_values, deduction):
    final_int = 0
    multiplier = [1000, 100, 10, 1]
    for idx, value in enumerate(output_values):
        translated_value = [n for n in deduction if deduction[n].get('final') == value][0]
        final_int += multiplier[idx] * translated_value
    return final_int
    

def deduct_mapping(entry):

    deduction = {k : {'regular' : set(signals[k])} for k in signals.keys()}
    mapping = {}
    #pprint.pprint(deduction)
    
    # collect hypotheses for all numbers:
    # based on length
    for number in deduction:
        deduction[number]['hypotheses'] = [pattern for pattern in entry.get('signal_patterns') if len(pattern) == len(deduction[number]['regular'])]
    update_deduction(deduction)     

    # infer more number from the ones with a unique length
    infer_numbers(deduction)
    
    # once we have all full numbers, extrapolate the segment mapping
    # we don't actually need this
    #mapping = {}
    #for letter in 'abcdefg':
    #    mapping[letter] = translate_letter(letter, deduction)

    return translate_output_values_to_int(entry.get('output_values'), deduction)

    
# -------------------------
# main
# -------------------------

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
    data.append({'signal_patterns' : [set(i) for i in inputlist[0:10]], 'output_values' : [set(i) for i in inputlist[11:]]})
#print()
#pprint.pprint(data)

print(sum([deduct_mapping(d) for d in data]))

def simulate_one_day(fish_dict):
    new_fish_dict = {}
    for i in range(9):
        new_fish_dict[i] = 0
    for k in fish_dict.keys():
        if k == 0:
            new_fish_dict[8] += fish_dict[k]
            new_fish_dict[6] += fish_dict[k]
        else:
            new_fish_dict[k-1] += fish_dict[k]
    return new_fish_dict

def fish_count(fish_dict):
    return sum(fish_dict.values())

# 6a code could not deal with more than 128 days of exponential growth
# idea: instead of using a list with all fishes, we use a list/dict of counters instead

fish_dict = {}
for i in range(9):
    fish_dict[i] = 0

with open('data/input_6.txt') as infile:
#with open('data/example_6.txt') as infile:
    fishes = [int(fish.strip()) for fish in infile.readline().split(",")]
    for f in fishes:
        fish_dict[f] += 1
        
    print(fish_dict)
    
for day in range(256):
    fish_dict = simulate_one_day(fish_dict)
    print("day", day, ":", fish_dict)
    print(fish_count(fish_dict))
    


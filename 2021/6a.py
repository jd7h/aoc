def simulate_one_day(fishes):
    new_fishes = []
    for fish in fishes:
        new_fish = fish-1
        if new_fish < 0:
            new_fish = 6
            new_fishes.append(8)       
        new_fishes.append(new_fish)
    return new_fishes

with open('data/input_6.txt') as infile:
#with open('data/example_6.txt') as infile:
    fishes = [int(fish.strip()) for fish in infile.readline().split(",")]
    
for day in range(80):
    fishes = simulate_one_day(fishes)
    print("day", day, ":", fishes)
    print(len(fishes))
    
# idee: in plaats van een lijst met alle vissen, een lijst met counters. 

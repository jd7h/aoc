def compute_fuel_needed_(crab_position, alignment_point):
    fuel_use = 0
    for i in range(abs(alignment_point - crab_position)):
        fuel_use += i+1
    return fuel_use
    
def compute_fuel_needed(d):
    return 0.5 * d * (d + 1)

with open('data/input_7.txt') as infile:
#with open('data/example_7.txt') as infile:
    data = [int(crab) for crab in infile.readline().split(",")]
    
print(data)

minimum_fuel_needed = len(data) * compute_fuel_needed(abs(min(data) - max(data))) # upper bound = nr of crabs * cost of reaching most far-away point
best_alignment_point = max(data)
for i in range(min(data), max(data)+1):
    fuel_needed = sum([compute_fuel_needed(abs(crab - i)) for crab in data])
    print("To align on space", i, "we need", fuel_needed, "fuel in total")
    if fuel_needed < minimum_fuel_needed:
        minimum_fuel_needed = fuel_needed
        best_alignment_point = i
        
print("Best solution: align on space", best_alignment_point, "with", minimum_fuel_needed, "fuel")

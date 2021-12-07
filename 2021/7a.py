with open('data/input_7.txt') as infile:
#with open('data/example_7.txt') as infile:
    data = [int(crab) for crab in infile.readline().split(",")]
    
print(data)

minimum_fuel_needed = len(data) * max(data) # upper bound = nr of crabs * most far-away point
best_alignment_point = max(data)
for i in range(min(data), max(data)+1):
    fuel_needed = sum([abs(i-crab) for crab in data])
    print("To align on space", i, "we need", fuel_needed, "fuel")
    if fuel_needed < minimum_fuel_needed:
        minimum_fuel_needed = fuel_needed
        best_alignment_point = i
        
print("Best solution: align on space", best_alignment_point, "with", minimum_fuel_needed, "fuel")

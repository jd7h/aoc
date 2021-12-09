import pprint

# read input
with open('data/input_9.txt') as infile:
#with open('data/example_9.txt') as infile:
    data = [[int(x) for x in list(line.strip())] for line in infile.readlines()]
# print(data)
print(sum([len(row) for row in data]), "coordinates read")

# find low points 
# relevant info: values of 4 neighbours (= lowpoint), and height+1

coordinfo = {}
for x in range(len(data)):
    for y in range(len(data[0])):
        coordinfo[(x,y)] = {}
        coordinfo[(x,y)]['height'] = data[x][y]
        coordinfo[(x,y)]['risk'] = data[x][y]+1
        coordinfo[(x,y)]['neighbour_heights'] = []
        coordinfo[(x,y)]['neighbour_coords'] = []
        if y > 0:
            coordinfo[(x,y)]['neighbour_coords'].append((x,y-1))
            coordinfo[(x,y)]['neighbour_heights'].append(data[x][y-1])
        if x > 0:
            coordinfo[(x,y)]['neighbour_coords'].append((x-1,y))
            coordinfo[(x,y)]['neighbour_heights'].append(data[x-1][y])
        if y < len(data[0])-1:
            coordinfo[(x,y)]['neighbour_coords'].append((x,y+1))
            coordinfo[(x,y)]['neighbour_heights'].append(data[x][y+1])
        if x < len(data)-1:
            coordinfo[(x,y)]['neighbour_coords'].append((x+1,y))
            coordinfo[(x,y)]['neighbour_heights'].append(data[x+1][y])
        coordinfo[(x,y)]['low_point'] = False
        if [n for n in coordinfo[(x,y)]['neighbour_heights'] if n <= coordinfo[(x,y)]['height']] == []:
            coordinfo[(x,y)]['low_point'] = True
        
print(len(coordinfo), "datapoints processed")
#pprint.pprint(coordinfo)

print("Low points:")
pprint.pprint([c for c in coordinfo if coordinfo[c]['low_point']])

# compute risk level
# sum risk levels
pprint.pprint(sum([coordinfo[c]['risk'] for c in coordinfo if coordinfo[c]['low_point']]))

# part B
basins = []
checked = set()
# search from the lowpoints outward
for c in [c for c in coordinfo if coordinfo[c]['low_point']]:
    queue = [c]
    basin = set()
    while queue != []:
        current = queue.pop(0)
        checked.update([current])
        if coordinfo[current]['height'] < 9:
            basin.update([current])
            queue.extend([n for n in coordinfo[current]['neighbour_coords'] if n not in basin and n not in checked])
    basins.append(basin)

# find three largest basins and multiply their size
basins.sort(key=lambda basin: len(basin))
result = 1
for size in [len(basin) for basin in basins[-3:]]:
    print(size)
    result *= size
print(result)


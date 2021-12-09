import pprint

# read input
with open('data/input_9.txt') as infile:
#with open('data/example_9.txt') as infile:
    data = [[int(x) for x in list(line.strip())] for line in infile.readlines()]
# print(data)
print(sum([len(row) for row in data]), "coordinates read")

# find low points 
# relevant info: values of 4 neighbours (= lowpoint), and height+1

coord_info = []
for x in range(len(data)):
    for y in range(len(data[0])):
        datapoint = {}
        datapoint['coordinates'] = (x,y)
        datapoint['height'] = data[x][y]
        datapoint['risk'] = data[x][y]+1
        datapoint['neighbours'] = []
        if y > 0:
            datapoint['neighbours'].append(data[x][y-1])
        if x > 0:
            datapoint['neighbours'].append(data[x-1][y])
        if y < len(data[0])-1:
            datapoint['neighbours'].append(data[x][y+1])
        if x < len(data)-1:
            datapoint['neighbours'].append(data[x+1][y])
        datapoint['low_point'] = False
        if [n for n in datapoint['neighbours'] if n <= datapoint['height']] == []:
            datapoint['low_point'] = True
        coord_info.append(datapoint)
        
print(len(coord_info), "datapoints processed")
        
pprint.pprint([c for c in coord_info if c['low_point']])
# compute risk level
# sum risk levels
pprint.pprint(sum([c['risk'] for c in coord_info if c['low_point']]))





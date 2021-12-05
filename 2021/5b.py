import pprint

def expand_spec_to_coordinates(spec):
    '''
    spec is one line of the input file
    and has the form "x1,y1 -> x2,y2"
    '''
    #print("Expanding spec", spec)
    start_coord, arrow, end_coord = spec.split(' ')
    start_x, start_y = start_coord.split(",")
    end_x, end_y = end_coord.split(",")
    start_x = int(start_x)
    start_y = int(start_y)
    end_x = int(end_x)
    end_y = int(end_y)
    
    points_in_line = []
    
    # define explicit step for range()
    step_x = 1
    step_y = 1
    if start_x > end_x:
        step_x = -1
    if start_y > end_y:
        step_y = -1
        
    if is_straight_line(start_x, start_y, end_x, end_y):
        for x in range(start_x, end_x+step_x, step_x):
            for y in range(start_y, end_y+step_y, step_y):
                #print(x,y)
                points_in_line.append((x, y)) 
    else:
        y = start_y
        for x in range(start_x, end_x+step_x, step_x):
            #print(x,y)
            points_in_line.append((x, y))
            y += step_y
        if y != end_y + step_y:
            raise Warning("y is now %d, but was expecting %d", y, end_y)
    return points_in_line
    
def is_straight_line(start_x, start_y, end_x, end_y):
    return start_x == end_x or start_y == end_y


with open('data/input_5.txt') as infile:
#with open('data/example_5.txt') as infile:
    specs = [line.strip() for line in infile.readlines()]
    #print("Specification:")
    #pprint.pprint(specs)
    lines = []
    for spec in specs:
        lines.append(expand_spec_to_coordinates(spec))
    #print("All coordinates:")
    #pprint.pprint(lines)
    lines_at_coord = {}
    for line in lines:
        for coord in line:
            if not coord in lines_at_coord:
                lines_at_coord[coord] = 0
            lines_at_coord[coord] += 1
    result = 0
    for amount in lines_at_coord.values():
        if amount >= 2:
            result += 1
    print("There are", result, "points where 2 lines or more overlap.")

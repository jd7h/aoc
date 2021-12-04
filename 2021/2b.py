with open('data/input_2.txt') as infile:
#with open('data/example_2.txt') as infile:
    data = [l.split()for l in infile.readlines()]
    
print(data)

position = {'horizontal_position' : 0, 'depth' : 0, 'aim' : 0}

for command, amount in data:
    amount = int(amount)
    if command not in ['forward','down','up']:
        raise ValueError()
    if command == 'forward':
        position['horizontal_position'] += amount
        position['depth'] += position['aim'] * amount
    elif command == 'down':
        position['aim'] += amount
    elif command == 'up':
        position['aim'] -= amount
        
print(position)
print("Answer:", position['horizontal_position'] * position['depth'])

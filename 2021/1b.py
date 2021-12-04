with open('data/input_1.txt') as infile:
#with open('data/example_1.txt') as infile:
    data = [int(l.strip()) for l in infile.readlines()]

print(len(data))

sliding_window = [sum([data[i], data[i+1], data[i+2]]) for i in range(0, len(data)-2)]
print(len(sliding_window))




increases = 0

for idx, sonar_reading in enumerate(sliding_window):
    increase = False
    if idx == 0:
        print(sonar_reading, increase)
        continue
    if sonar_reading > sliding_window[idx-1]:
        increase = True
        increases += 1
    print(sonar_reading, increase)

print(increases)



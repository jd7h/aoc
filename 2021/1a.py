
with open('data/input_1.txt') as infile:
#with open('data/example_1.txt') as infile:
    data = [int(l.strip()) for l in infile.readlines()]

print(len(data))

increases = 0

for idx, sonar_reading in enumerate(data):
    increase = False
    if idx == 0:
        print(sonar_reading, increase)
        continue
    if sonar_reading > data[idx-1]:
        increase = True
        increases += 1
    print(sonar_reading, increase)

print(increases)



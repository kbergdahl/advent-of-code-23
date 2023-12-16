import numpy as np

# Read data
#data_source = 'day11/example_data.txt'
data_source = 'day11/data.txt'

with open(data_source) as f:
    lines = f.read().split('\n')

half_expanded = []

# Convert to 0 and numbers and expand rows at the same time
current_galaxy = 1
for line in lines:
    if '#' in line:
        current_line = []
        for symbol in line:
            if symbol == '.':
                current_line.append(0)
            else:
                current_line.append(current_galaxy)
                current_galaxy += 1
        half_expanded.append(current_line)
    else:
        half_expanded.append([0 for a in line])
        half_expanded.append([0 for a in line])

half_expanded = np.array(half_expanded)

# Expand columns
half_expanded = np.transpose(half_expanded)
expanded = []
for line in half_expanded:
    if np.any(line):
        expanded.append(line)
    else:
        expanded.append(line)
        expanded.append(line)

expanded = np.array(expanded)
expanded = np.transpose(expanded)

# Find distance between each pair
sum = 0

coordinates = np.nonzero(expanded)
coordinates = list(zip(coordinates[0], coordinates[1]))

for ind, gal1 in enumerate(coordinates):
    for gal2 in coordinates[(ind+1):]:
        sum += np.abs(gal2[0] - gal1[0]) + np.abs(gal2[1] - gal1[1])

print("The solution to puzzle 1 is: " + str(sum))

#######################################################

# Instead of actually making the matrix that large, just store the indexes of the empty lines and columns

# Convert to 0 and numbers and save empty rows
myMap = []
current_galaxy = 1
empty_rows = []
for ind, line in enumerate(lines):
    if '#' in line:
        current_line = []
        for symbol in line:
            if symbol == '.':
                current_line.append(0)
            else:
                current_line.append(current_galaxy)
                current_galaxy += 1
        myMap.append(current_line)
    else:
        myMap.append([0 for a in line])
        empty_rows.append(ind)

# Find empty columns
myMap = np.array(myMap)
myMap = np.transpose(myMap)

empty_cols = []
for ind, line in enumerate(myMap):
    if not np.any(line):
        empty_cols.append(ind)

myMap = np.transpose(myMap)


# Find distance between each pair
exp_factor = 1000000
sum = 0

coordinates = np.nonzero(myMap)
coordinates = list(zip(coordinates[0], coordinates[1]))

for ind, gal1 in enumerate(coordinates):
    for gal2 in coordinates[(ind+1):]:

        # Add empty rows
        for ind in empty_rows:
            if (ind < gal2[0] and ind > gal1[0]) or (ind > gal2[0] and ind < gal1[0]):
                sum += (exp_factor - 1)
        
        # Add empty columns
        for ind in empty_cols:
            if (ind < gal2[1] and ind > gal1[1]) or (ind > gal2[1] and ind < gal1[1]):
                sum += (exp_factor - 1)

        sum += np.abs(gal2[0] - gal1[0]) + np.abs(gal2[1] - gal1[1])

print("The solution to puzzle 2 is: " + str(sum))
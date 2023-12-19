import numpy as np

# Read data
#data_source = 'day14/example_data.txt'
data_source = 'day14/data.txt'

with open(data_source) as f:
    myMap = f.read().split('\n')

# Convert to numpy array to make it easy to read columns
myMap = [[*row] for row in myMap]
myMap = np.array(myMap)

for row in np.transpose(myMap):
    free_spaces = []
    for pos, symbol in enumerate(row):
        match symbol:
            case '.':
                free_spaces = free_spaces + [pos]

            case '#':
                free_spaces = []
            
            case 'O':
                if free_spaces:
                    row[free_spaces[0]] = 'O'
                    row[pos] = '.'

                    # Now it depends on what is left in the list
                    if len(free_spaces) > 1:
                        free_spaces = free_spaces[1:] + [pos]
                    else:
                        free_spaces = [pos]


rows, cols = myMap.shape
_, weights = np.meshgrid(np.arange(0,rows), np.arange(cols, 0, -1))

print("The answer to puzzle 1 is: " + str(np.sum(np.where(myMap == 'O', weights, 0))))

####################################
def roll(rock_map, direction):
    # Do a westward roll of the map input
    match direction:
        case 'n':
            rock_map = np.transpose(rock_map)
        case 's':
            rock_map = np.fliplr(np.transpose(rock_map))
        case 'e':
            rock_map = np.fliplr(rock_map)
    for row in rock_map:
        free_spaces = []
        for pos, symbol in enumerate(row):
            match symbol:
                case '.':
                    free_spaces = free_spaces + [pos]

                case '#':
                    free_spaces = []
                
                case 'O':
                    if free_spaces:
                        row[free_spaces[0]] = 'O'
                        row[pos] = '.'

                        # Now it depends on what is left in the list
                        if len(free_spaces) > 1:
                            free_spaces = free_spaces[1:] + [pos]
                        else:
                            free_spaces = [pos]
    match direction:
        case 'n':
            rock_map = np.transpose(rock_map)
        case 's':
            rock_map = np.transpose(np.fliplr(rock_map))
        case 'e':
            rock_map = np.fliplr(rock_map)
    return(rock_map)

def spincycle(rock_map):
    # Do a roll north, west, south, east
    rock_map = roll(rock_map, 'n')
    rock_map = roll(rock_map, 'w')
    rock_map = roll(rock_map, 's')
    rock_map = roll(rock_map, 'e')
    return rock_map

ammount = 0
prev_maps = []
rock_map = np.copy(myMap)
for i in range(1000000):
    rock_map = spincycle(rock_map)
    mapstring = rock_map.tobytes()
    if mapstring in prev_maps:
        initial_steps = prev_maps.index(mapstring)
        cycle_length = i - initial_steps
        break
    else:
        prev_maps.append(mapstring)

remaining_cycles = (1000000000 - initial_steps) % cycle_length
new_map = np.copy(myMap)
for i in range(initial_steps + remaining_cycles):
    new_map = spincycle(new_map)

print("The answer to puzzle 2 is: " + str(np.sum(np.where(new_map == 'O', weights, 0))))
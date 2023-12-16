import numpy as np

# Read data
#data_source = 'day8/example_data.txt'
data_source = 'day8/data.txt'

with open(data_source) as f:
    lines = f.read().split('\n')


# Process data
instructions = lines[0]
paths = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

# Take a ste along the path
def take_step(node, direction):
    if direction == 'L':
        return paths[node][0]
    
    else:
        return paths[node][1]

# Do the stepping
step_count = 0
current_node = 'AAA'
direction_len = len(instructions)

while current_node != 'ZZZ':
    direction = instructions[step_count % direction_len]
    current_node = take_step(current_node, direction)
    step_count += 1

print("Solution to puzzle 1 is: " + str(step_count))

############
# This is a very ugly solution

# Checked my data, there are 6 nodes ending on A
ending_on_a = [key for key in dict.keys(paths) if key[2] == 'A']

# Checking to see if the "circles" seem to be consistent lengths
""" 
for node in ending_on_a:
    print(node)
    step_count = 0
    current_node = node
    direction_len = len(instructions)

    previous_hit = 0

    while step_count < 1000000:
        direction = instructions[step_count % direction_len]
        current_node = take_step(current_node, direction)
        step_count += 1

        if current_node[2] == 'Z':
            print(step_count - previous_hit)
            previous_hit = step_count
 """
# They seem to be, so we use LCM
my_loops = [12083, 17141, 19951, 22199, 20513, 14893]

# Getting some overflow error applying reduce to the whole thing so split in half
lcm = 1
for item in my_loops:
    lcm = np.lcm(lcm, item, dtype=np.int64)
    print(lcm)
    print(type(lcm))

print("The answer to puzzle 2 is: " + str(lcm))

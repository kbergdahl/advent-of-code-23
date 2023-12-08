import numpy as np

# Read data
# data_source = 'day5/example_data.txt'
data_source = 'day5/data.txt'

with open(data_source) as f:
    lines = f.read().split("\n\n")

seeds = lines[0]
maps = lines[1:]

# Make seeds into an np.array of the seed numbers
seeds = seeds[7:] #(remove 'seeds: ' from the string)
seeds = np.fromstring(seeds, sep=' ')

def transform_map(og_map):
    # Process each map to be an np.array with columns [source_start source_end difference]
    # start_source - start of the source range
    # end_source - end of the source range
    # difference - how much to add to get the destination
    # og_map is an np.array with columns [dest_start source_start range_length]

    return np.transpose(np.array([og_map[:,1], og_map[:,1]+og_map[:,2]-1, og_map[:,0]-og_map[:,1]]))

# Create a dictionary of the maps
map_dict = {}
for entry in maps:
    entry = entry.splitlines()
    title = entry[0]
    values = entry[1:]
    new_values = np.array([np.fromstring(line, sep=' ') for line in values])
    map_dict[title] = transform_map(new_values)

categories = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

def run_mapping(inputs, map):
    # Taking an array out inputs (for example seed numbers) and a mapping to the next category
    # Giving an output to the next category

    outputs = np.copy(inputs)

    for row, input in enumerate(inputs):
        for map_part in map:
            if ((input >= (map_part[0])) and (input <= int(map_part[1]))):
                outputs[row] = input + map_part[2]

    return outputs

setup_matrix = np.zeros((len(seeds), len(categories)))
setup_matrix[:, 0] = seeds

for col, key in enumerate(map_dict):
    setup_matrix[:, col+1] = run_mapping(setup_matrix[:, col], map_dict[key])

print("The solution to puzzle 1 is: " + str(int(np.min(setup_matrix[:, -1]))))

###########################################################
# PART 2
###########################################################

# Recursive function to take in one range, output a number of ranges based on the map
def run_range_mapping(input_range, map):
    # Input: inputs_range, tuple of start and end of input

    # 5 cases: r_start m_start m_end r_end - map overlapped by range
    # r_start m_start r_end m_end - map low end cover
    # m_start r_start r-end m-end - range overlapped by map (Will give only one range)
    # m_start r_start m_end r_end - map high end cover
    # no overlap

    for map_part in map:
        # Range overlapped by map (base case)
        if ((input_range[0] >= map_part[0]) and (input_range[1] <= map_part[1])):
            return [(input_range[0] + map_part[2], input_range[1] + map_part[2])]
        
        # map low end cover
        elif ((input_range[0] < map_part[0]) and (input_range[1] >= map_part[0]) and (input_range[1] <= map_part[1])):
            lower_range = (input_range[0], map_part[0]-1)
            mapped_range = [(map_part[0] + map_part[2], input_range[1] + map_part[2])]
            return mapped_range + run_range_mapping(lower_range, map)
        
        # map high end cover
        elif ((input_range[0] >= map_part[0]) and (input_range[0] <= map_part[1]) and (input_range[1] > map_part[1])):
            higher_range = (map_part[1]+1, input_range[1])
            mapped_range = [(input_range[0] + map_part[2], map_part[1] + map_part[2])]
            return mapped_range + run_range_mapping(higher_range, map)
        
        # map overlapped by range
        elif ((input_range[0] < map_part[0]) and (input_range[1] > map_part[1])):
            lower_range = (input_range[0], map_part[0]-1)
            higher_range = (map_part[1]+1, input_range[1])
            mapped_range = [(map_part[0] + map_part[2], map_part[1] + map_part[2])]
            return mapped_range + run_range_mapping(higher_range, map)+ run_range_mapping(lower_range, map)
        
    # no overlap with any map
    return [input_range]

thing = run_range_mapping((25, 99), map_dict['seed-to-soil map:'])

# A dictionary with lists of tuples in each category
ranges = {}

# Set up tuples that define the ranges of seeds we use
seed_pairs = np.reshape(seeds, (-1, 2))
seed_pairs[:, 1] = seed_pairs[:, 0] + seed_pairs[:, 1] - 1
ranges[categories[0]] = list(map(tuple, seed_pairs))

for i, key in enumerate(map_dict):
    inputs = ranges[categories[i]]

    outputs = []

    for input in inputs:
        outputs += run_range_mapping(input, map_dict[key])
    
    ranges[categories[i+1]] = outputs

print("The answer to puzzle 2 is: " + str(int(min([item for t in ranges['location'] for item in t]))))
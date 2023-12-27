# Read data
#data_source = 'day19/example_data.txt'
data_source = 'day19/data.txt'

with open(data_source) as f:
    flows_list, parts_list = f.read().split('\n\n')

# Create the parts
def create_part_dict(str):
    part = {}
    str = str[1:-1]
    attributes = str.split(',')
    for item in attributes:
        part[item[0]] = int(item[2:])
    return part

parts_list = parts_list.split('\n')
parts = list(map(create_part_dict, parts_list))

# Create the flows
flows = {}
for flow in flows_list.split('\n'):
    name, instructions = flow.split('{')

    # Create a list for the flows, list item on the form (attribute to check, less or more, value, go to flow)
    flows[name] = []
    for item in instructions.split(','):
        if '}' in item:
            flows[name].append((None, None, None, item[0:-1]))
        else:
            cond, new_flow = item.split(':')
            flows[name].append((cond[0], cond[1], int(cond[2:]), new_flow))

# Function that takes a flow plus a part and returns the flow the part should go to
def parse_flow(flow, part):
    for cond in flow:
        match cond[1]:
            case '<':
                if part[cond[0]] < cond[2]: return cond[3]
            case '>':
                if part[cond[0]] > cond[2]: return cond[3]
            case _:
                return cond[3]

# Run the parts through the flow and sum the attributes of the accepted
sum = 0
for part in parts:
    flow_name = 'in'

    while flow_name != 'R' and flow_name != 'A':
        flow_name = parse_flow(flows[flow_name], part)
    
    if flow_name == 'A':
        for key in part:
            sum += part[key]

# Sum all attributes of all the accepted
print("The solution to puzzle 1 is: " + str(sum))

########################################################################
# These are the initial possible ranges
potential_parts = {'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1, 4000)}

def cut_range(cond, potential_parts):
    passingParts = potential_parts.copy()
    failingParts = potential_parts.copy()
    # THis takes a condition and a part with ranges, and cuts those ranges according to the condition
    match cond[1]:
        case '<':
            old_min, old_max = passingParts[cond[0]]
            new_max = cond[2] - 1
            if new_max < old_min:
                passingParts[cond[0]] = None
            elif new_max < old_max:
                passingParts[cond[0]] = (old_min, new_max)
                failingParts[cond[0]] = (new_max + 1, old_max)
            else:
                failingParts[cond[0]] = None
        case '>':
            old_min, old_max = passingParts[cond[0]]
            new_min = cond[2] + 1
            if new_min > old_max:
                passingParts[cond[0]] = None
            elif new_min > old_min:
                passingParts[cond[0]] = (new_min, old_max)
                failingParts[cond[0]] = (old_min, new_min - 1)
            else:
                failingParts[cond[0]] = None
        case _:
            # There is no comparison, everything passes, put None somewhere in failing so it gets sorted away
            failingParts['x'] = None
    return passingParts, failingParts

# Recursive function to cut down the potential ranges ending in acceptance
def get_potential_ranges(flow_name, part):
    if any(ran == None for ran in part.values()):
        return []
    if flow_name == 'A':
        return [part]
    elif flow_name == 'R':
        return []

    flow = flows[flow_name]
    returns = []
    for cond in flow:
        new_part, part = cut_range(cond, part)
        returns = returns + get_potential_ranges(cond[3], new_part)
    return returns

potential_parts = get_potential_ranges('in', potential_parts)

# Sum up number of potential parts
sum = 0
for item in potential_parts:
    add = 1
    for key in item:
        add *= (item[key][1] - item[key][0] + 1)
    sum += add
print("The solution to puzzle 2 is: " + str(sum))
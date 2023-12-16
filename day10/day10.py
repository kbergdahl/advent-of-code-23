import numpy as np

# Read data
#data_source = 'day10/example_data.txt'
data_source = 'day10/data.txt'

with open(data_source) as f:
    myMap = f.read().split('\n')

# Find starting point
for row, line in enumerate(myMap):
    for col, item in enumerate(line):
        if item == 'S':
            start = (row, col)

def find_connections(symbol, pos):
    # Given a symbol and the position of it, return the position of points connected by that symbol
    match symbol:
        case '|':
            return [(pos[0]-1, pos[1]), (pos[0]+1, pos[1])]
        case '-':
            return [(pos[0], pos[1]-1), (pos[0], pos[1]+1)]
        case 'L':
            return [(pos[0]-1, pos[1]), (pos[0], pos[1]+1)]
        case 'J':
            return [(pos[0]-1, pos[1]), (pos[0], pos[1]-1)]
        case '7':
            return [(pos[0]+1, pos[1]), (pos[0], pos[1]-1)]
        case 'F':
            return [(pos[0]+1, pos[1]), (pos[0], pos[1]+1)]
        case '.':
            return []

def one_step(current_pos, goal_pos, goal_symbol):
    # you are at current, want to go to adjacent position 'goal'
    # Look at the symbol at goal, see if it is connected to current position
    # If so, return new current and goal
    connections = find_connections(goal_symbol, goal_pos)
    if connections:
        if current_pos == connections[0]:
            return (goal_pos, connections[1])
        else:
            return (goal_pos, connections[0])
    else:
        return None, None

possible_directions = [
    (start[0]+1, start[1]),
    (start[0]-1, start[1]),
    (start[0], start[1]+1),
    (start[0], start[1]-1)
]

for start_goal in possible_directions:
    steps = 0
    goal_symbol = myMap[start_goal[0]][start_goal[1]]
    current_pos = start
    goal_pos = start_goal

    while goal_symbol != 'S':
        # Stop if we have to go out of the grid
        if goal_pos[0] < 0 or goal_pos[1] < 0:
            break

        current_pos, goal_pos = one_step(current_pos, goal_pos, goal_symbol)
        if current_pos:
            goal_symbol = myMap[goal_pos[0]][goal_pos[1]]
            steps += 1

        # Stop if there was not connection
        else:
            break
    print("End of trial, furthest point: " + str((steps+1)/2))
print("The solution should be the one that there are two of among the trials")

##################################################
# PART 2 DOES NOT WORK
# I found going with the first start works for my input
# Traverse through that course to create a numerated path

myPath = np.zeros((len(myMap), len(myMap[0])))

step = 2
goal_pos = possible_directions[0]
goal_symbol = myMap[goal_pos[0]][goal_pos[1]]
current_pos = start


while goal_symbol != 'S':
    myPath[current_pos[0], current_pos[1]] = step

    current_pos, goal_pos = one_step(current_pos, goal_pos, goal_symbol)
    if current_pos:
        goal_symbol = myMap[goal_pos[0]][goal_pos[1]]
        step += 1
myPath[current_pos[0], current_pos[1]] = step

# We need to know the difference of the start and end step to be able to connect them
end_value = np.max(myPath)

# Conditions under which the path continues to the left
def path_continues(line, ind):
    is_start_end = line[ind] == 2 and line[ind+1] == end_value
    is_adjacent = np.abs(line[ind] - line[ind+1]) == 1
    return is_start_end or is_adjacent

inside = False
sum = 0
for row, line in enumerate(myPath):
    # If we have crossed the path an odd number of times, we are inside.
    # If we have crossed it an even number of times, we are outside

    # When there is more than one part of the path in a row, we have to know if the path is crossing or turning at our line
    first_in_segment = True

    for col, point in enumerate(line):
        if point == 0 and inside:
            sum += 1
        elif point > 0:
            # If this is the start of a segment
            if col == 0 or (np.abs(line[col] - line[col-1]) > 2 and np.abs(line[col] - line[col-1]) < (end_value-2)):
                # Find the end of this segment
                end_col = col
                seg_len = 1
                while (col + seg_len) < len(line) and path_continues(line, col+seg_len-1):
                    seg_len += 1
                
                # Check if this crosses or turns and toggle inside if it does
                # Cannot cross if we are at the top or bottom
                if row == 0 or row == (len(myPath)-1):
                    pass
                # Definitely crosses if the segment is just 1
                elif seg_len == 1:
                    inside = not inside
                else:
                    come_from_above = np.abs(myPath[row-1][col] - point) < 2
                    go_to_above = np.abs(myPath[row-1][col+seg_len-1] - myPath[row][col+seg_len-1]) < 2
                    if come_from_above != go_to_above:
                        inside = not inside

print(sum)
import numpy as np

# Read data
data_source = 'day10/example_data.txt'
#data_source = 'day10/data.txt'

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
print(" The solution should be the one that there are two of among the trials")


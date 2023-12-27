from heapq import heappop, heappush

# Idea from another person: use complex numbers to store position/direction

# Read data
#data_source = 'day17/example_data.txt'
data_source = 'day17/data.txt'

with open(data_source) as f:
    myMap = f.read().split('\n')

# Make a dictionary of the positions in the grid and their values
G = {row + col*1j: int(value) for row, line in enumerate(myMap) for col, value in enumerate(line)}

# Todo list and seen set
# Since we want to sort on lowest value, it is formated as (value, (entry count to allow heap to sort), position, direction
todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
seen = set()
entry = 0
end = [*G][-1]

while todo:
    val, _, pos, dir = heappop(todo)

    if pos == end:
        print("The solution to puzzle 1 is: " + str(val))
        break

    if (pos, dir) in seen: continue

    seen.add((pos, dir))

    # Check both ways to turn
    for d in 1j/dir, -1j/dir:
        for steps in range(1, 4):
            if pos + d*steps in G:
                # Sum the values along the steps
                v = sum(G[pos + d*a] for a in range(1, steps+1))
                heappush(todo, (val + v, (entry:=entry+1), pos + d*steps, d))

##################################
                
# Todo list and seen set
# Since we want to sort on lowest value, it is formated as (value, (entry count to allow heap to sort), position, direction
todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
seen = set()
entry = 0
end = [*G][-1]

while todo:
    val, _, pos, dir = heappop(todo)

    if pos == end:
        print("The solution to puzzle 2 is: " + str(val))
        break

    if (pos, dir) in seen: continue

    seen.add((pos, dir))

    # Check both ways to turn
    for d in 1j/dir, -1j/dir:
        for steps in range(4, 11):
            if pos + d*steps in G:
                # Sum the values along the steps
                v = sum(G[pos + d*a] for a in range(1, steps+1))
                heappush(todo, (val + v, (entry:=entry+1), pos + d*steps, d))
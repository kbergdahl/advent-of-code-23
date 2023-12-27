import numpy as np

# Read data
#data_source = 'day18/example_data.txt'
data_source = 'day18/data.txt'

with open(data_source) as f:
    instructions = f.read().split('\n')

# Again use complex numbers to represent directions (row = real part, col = imaginary part)
dug = []
pos = 0 + 0j
nbr_edge_points = 0

def dir_to_diff(dir):
    match dir:
        case 'U': return -1
        case 'D': return 1
        case 'R': return 1j
        case 'L': return -1j

# Start with digging
for line in instructions:
    dir, dist, _ = line.split()

    # Convert direction and distance
    dir = dir_to_diff(dir)
    dist = int(dist)
    nbr_edge_points += dist

    pos = pos + dir*dist
    dug.append(pos)


# Use shoelace formula and  Pick's theorem
# Shoelace to get area A defined by the vertices
area = sum([dug[i].imag * (dug[i+1].real - dug[i-1].real) for i in range(-1, len(dug)-1)]) / 2

# Pick's
# A = i + b/2 - 1
# We know b and A, want to solve for i
# i = A - b/2 + 1

interior = area - nbr_edge_points/2 + 1
print("The solution to puzzle 1 is: " + str(int(interior + nbr_edge_points)))

######################################################################33
dug = []
pos = 0 + 0j
nbr_edge_points = 0

# Different way of finding step and direction
def nbr_dir_to_diff(dir):
    match dir:
        case '0': return 1j
        case '1': return 1
        case '2': return -1j
        case '3': return -1


for line in instructions:
    _, _, info = line.split()

    # Convert direction and distance
    dir = nbr_dir_to_diff(info[7])
    dist = int(info[2:7], 16)
    nbr_edge_points += dist

    pos = pos + dir*dist
    dug.append(pos)

# Use shoelace formula and  Pick's theorem
# Shoelace to get area A defined by the vertices
area = sum([dug[i].imag * (dug[i+1].real - dug[i-1].real) for i in range(-1, len(dug)-1)]) / 2

# Pick's
# A = i + b/2 - 1
# We know b and A, want to solve for i
# i = A - b/2 + 1

interior = area - nbr_edge_points/2 + 1
print("The solution to puzzle 2 is: " + str(int(interior + nbr_edge_points)))
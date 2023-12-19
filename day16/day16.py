import numpy as np
import sys

# Set recursion limit
sys.setrecursionlimit(10000)

# Read data
#data_source = 'day16/example_data.txt'
data_source = 'day16/data.txt'

with open(data_source) as f:
    myMap = f.read().split('\n')

myMap = [list(string) for string in myMap]
myMap = np.array(myMap)
done_beams = []
max_row, max_col = myMap.shape
energized = np.zeros((max_row, max_col))

def take_step(pos, dir):
    row, col = pos
    if (pos, dir) in done_beams:
        return
    else:
        done_beams.append((pos, dir))
        energized[row, col] = 1
        match myMap[row, col]:
            case '.':
                new_dir = [dir]
            case '\\':
                match dir:
                    case 'r':
                        new_dir = ['d']
                    case 'l':
                        new_dir = ['u']
                    case 'd':
                        new_dir = ['r']
                    case 'u':
                        new_dir = ['l']
            case '/':
                match dir:
                    case 'r':
                        new_dir = ['u']
                    case 'l':
                        new_dir = ['d']
                    case 'd':
                        new_dir = ['l']
                    case 'u':
                        new_dir = ['r']
            case '|':
                match dir:
                    case 'u'|'d':
                        new_dir = [dir]
                    case 'l'|'r':
                        new_dir = ['u', 'd']
            case '-':
                match dir:
                    case 'u'|'d':
                        new_dir = ['l', 'r']
                    case 'l'|'r':
                        new_dir = [dir]            
        for dir1 in new_dir:
            match dir1:
                case 'r':
                    new_row = row
                    new_col = col + 1
                case 'l':
                    new_row = row
                    new_col = col - 1
                case 'u':
                    new_row = row - 1
                    new_col = col
                case 'd':
                    new_row = row + 1
                    new_col = col

            if new_row >= 0 and new_col >= 0 and new_row < max_row and new_col < max_col:
                take_step((new_row, new_col), dir1)
        return

take_step((0, 0), 'r')
print("The solution to puzzle 1 is: " + str(int(np.sum(energized))))

# Part 2
max_energy = 0

# Start on upper edge, go down
for col in range(max_col):
    energized.fill(0)
    done_beams = []
    take_step((0, col), 'd')
    energy = np.sum(energized)
    if energy > max_energy:
        max_energy = energy

# Start on left edge, go right
for row in range(max_row):
    energized.fill(0)
    done_beams = []
    take_step((row, 0), 'r')
    energy = np.sum(energized)
    if energy > max_energy:
        max_energy = energy

# Start on lower edge, go up
for col in range(max_col):
    energized.fill(0)
    done_beams = []
    take_step((max_row-1, col), 'u')
    energy = np.sum(energized)
    if energy > max_energy:
        max_energy = energy

# Start on right edge, go left
for row in range(max_row):
    energized.fill(0)
    done_beams = []
    take_step((row, max_col-1), 'l')
    energy = np.sum(energized)
    if energy > max_energy:
        max_energy = energy

print("The solution to puzzle 2 is: " + str(int(max_energy)))
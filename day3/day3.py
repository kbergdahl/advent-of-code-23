import numpy as np

# Read data
with open('day3/data.txt') as f:
    lines = f.read().splitlines()

# Example data
""" lines = ["467..114..",
         "...*......",
         "..35..633.",
         "......#...",
         "617*......",
         ".....+.58.",
         "..592.....",
         "......755.",
         "...$.*....",
         ".664.598.."] """

# The idea: each value in the grid gets an id
# Create a matrix with the id in the spot of the number, 0 as ., -1 as other symbols
# Create a list with id-value pairings

matrix_size = (len(lines), len(lines[0]))
id_matrix = np.zeros(matrix_size)

id = 0

# Create id_matrix
for row, line in enumerate(lines):

    # At the start of each line, reset prev_was_dig (a number cannot stretch over 2 lines
    prev_was_dig = False
    for col, character in enumerate(line):

        # For digits, give id
        if character.isdigit():
            if prev_was_dig:
                id_matrix[row][col] = id
            
            else:
                id += 1
                id_matrix[row][col] = id
            
            prev_was_dig = True
        
        # For periods, set id_matrix to -1, previous character was not digit
        elif (character == '.'):
            prev_was_dig = False
            id_matrix[row][col] = -1
        
        # For other symbols, previous character was not digit, let id_matrix be 0
        else:
            prev_was_dig = False


def surround_prod(row, col, matrix, matrix_size):
    # Different cases for edges vs middle of matrix
    if row == 0:
        if col == 0:
            return np.prod(matrix[:2, :2])
        elif (col == (matrix_size[1]-1)):
            return np.prod(matrix[:2, -2:])
        else:
            return np.prod(matrix[:2, (col-1):(col+2)])
    
    elif row == (matrix_size[0]-1):
        if col == 0:
            return np.prod(matrix[-2:, :2])
        elif (col == (matrix_size[1]-1)):
            return np.prod(matrix[-2:, -2:])
        else:
            return np.prod(matrix[-2:, (col-1):(col+2)])
    
    else:
        return np.prod(matrix[(row-1):(row+2), (col-1):(col+2)])

# Touching matrix has True in all spots that touch a symbol
touching_matrix = np.zeros(matrix_size)
for row, line in enumerate(lines):
    for col, _ in enumerate(line):
        touching_matrix[row][col] = surround_prod(row, col, id_matrix, matrix_size)

touching_matrix = (touching_matrix == 0)


values = [0]
sum = 0
for row, line in enumerate(lines):
    col = 0
    while (col < matrix_size[1]):
        # If the character is a digit, find the whole number
        if line[col].isdigit():
            value = int(line[col])
            nbr_len = 1
            touching = touching_matrix[row, col]

            # Find value and length of number
            while (col+nbr_len < matrix_size[1] and line[col+nbr_len].isdigit()):
                value = value*10 + int(line[col+nbr_len])

                # Check in touching matrix if the this digit of the number (and thus the whole number) is touching a symbol
                if touching_matrix[row, (col+nbr_len)]:
                    touching = True

                nbr_len += 1

            # If the number is touching a symbol, add it to the total
            if touching:
                sum += value
            
            # Also add the number to the id - value list for problem 2
            values.append(value)

            # Skip the rest of the number in the iteration
            col += nbr_len-1

        col += 1

print("The solution to puzzle 1 is: " + str(sum))

############################################################
# PART 2
############################################################

# We already have id_matrix, which has unique ids for each number in the grid
# And the values list, which connects id to value
# That will help us identify which * is touching exactly 2 numbers

def look_around(row, col, id_matrix, matrix_size):
    # Looks around a spot (row, col), returns a list of the ids found around that spot from id_matrix
    
    # Different cases for edges/corners
    if row == 0:
        if col == 0:
            surroundings = id_matrix[:2, :2]
        elif (col == (matrix_size[1]-1)):
            surroundings = id_matrix[:2, -2:]
        else:
            surroundings = id_matrix[:2, (col-1):(col+2)]
    
    elif row == (matrix_size[0]-1):
        if col == 0:
            surroundings = id_matrix[-2:, :2]
        elif (col == (matrix_size[1]-1)):
            surroundings = id_matrix[-2:, -2:]
        else:
            surroundings = id_matrix[-2:, (col-1):(col+2)]
    
    else:
        surroundings = id_matrix[(row-1):(row+2), (col-1):(col+2)]
    
    # Flatten remove duplicates, remove 0 and negatives
    surroundings = np.unique(surroundings.flatten())
    return surroundings[surroundings > 0]
            

sum = 0

for row, line in enumerate(lines):
    for col, character in enumerate(line):
        if (character == '*'):
            # Get a list of the ids the * is touching
            ids = look_around(row, col, id_matrix, matrix_size)

            # If it is touching exactly 2, add the product to the sum
            if (len(ids)==2):
                sum += values[int(ids[0])]*values[int(ids[1])]

print("The solution to puzzle 2 is: " + str(sum))
